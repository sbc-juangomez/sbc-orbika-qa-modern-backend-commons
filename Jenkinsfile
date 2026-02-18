import groovy.json.JsonOutput

pipeline {
    agent any

    environment {
        AWS_REGION = 'us-east-1'
        pipelineName = env.JOB_NAME.replace('/', '/job/')
    }

    parameters {
        choice(name: 'ENVIRONMENT', choices: ['dev','qa','mock'], description: 'Specify the environment: dev or qa or mock')
        choice(name: 'FUNCTIONALITY', choices: [ 'login'], description: 'Specify the functionality: login or service_order')
        choice(name:'LABEL_SCENARIO',choices:[ 'all_login'],description:'Specifythetestscenario')
        choice(name: 'CHANGE_MOCK_VARIABLES', choices: ['NO','SI'], description: 'Change lambdas variables to mock')
        choice(name: 'LOG_LEVEL', choices: ['DEBUG','INFO','WARNING','ERROR','CRITICAL'], description: 'Specify the log level')
    }

    stages {
        stage('Clean Previous Virtual Env') {
            steps {
                script {
                    sh '''
                    if [ -d "$(pwd)/venv" ];then
                    rm -rf $(pwd)/venv
                    fi
                    '''
                }
            }
        }

        stage('Clean Previous Allure Results') {
            steps {
                script {
                    sh 'rm -rf $(pwd)/target/allure-results'
                }
            }
        }

//         stage('SonarQube Analysis') {
//              steps {
//                  script {
//                      def scannerHome = tool 'Subocol-SonarQubeScanner'
//                      withSonarQubeEnv('SonarQube-Subocol') {
//                          sh "${scannerHome}/bin/sonar-scanner"
//                     }
//                  }
//              }
//          }

        stage('Setup AWS Credentials') {
            steps {
                script {
                    def credentialsId = params.ENVIRONMENT == 'qa' ? 'CREDENTIALS_QA' : 'CREDENTIALS_DEV'

                    withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: credentialsId]]) {
                        env.AWS_ACCESS_KEY_ID = "${AWS_ACCESS_KEY_ID}"
                        env.AWS_SECRET_ACCESS_KEY = "${AWS_SECRET_ACCESS_KEY}"
                        sh '''
                            echo "Setting AWS credentials"
                            echo "AWS_ACCESS_KEY_ID: $AWS_ACCESS_KEY_ID"
                            echo "AWS_SECRET_ACCESS_KEY: $AWS_SECRET_ACCESS_KEY"
                        '''
                    }
                }
            }
        }

        stage('Setup Python environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                '''
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                    . venv/bin/activate
                    pip install pytest allure-pytest requests psycopg2-binary boto3 pytest-ordering pytz
                    pip install pyotp
                '''
            }
        }

        stage('Pre-Test Setup') {
            when {
                expression { params.CHANGE_MOCK_VARIABLES == 'SI' }
            }
            steps {
                script {
                    sh '''
                        . venv/bin/activate
                        python -c "from src.orbika.facts.aws.fact_conditions_test_aws import FactConditionsTestsAws; FactConditionsTestsAws().fact_change_lambda_params('cognito', False)"
                    '''
                }
            }
        }

        stage('Run tests') {
            steps {
                script {
              // Leer el archivo JSON
                def testFiles = readJSON file: 'testFiles.json'
                echo "Test files: ${testFiles}"

                // Inicializar la variable donde se almacenarán los archivos que coincidan con el LABEL_SCENARIO
                def filesToTest = []

                // Asegurarse de que estamos accediendo correctamente a la lista bajo la clave 'testFiles'
                def testFilesList = testFiles.testFiles  // Asumir que 'testFiles' es la clave que contiene el mapa

                // Iterar sobre el mapa testFiles
                testFilesList.each { labelScenario, filePaths ->

                    // Comparar la clave del archivo con el LABEL_SCENARIO
                    if (labelScenario == params.LABEL_SCENARIO) {
                        // Si la clave coincide con LABEL_SCENARIO, verificar si filePaths es una lista
                        if (filePaths instanceof List) {
                            // Si es una lista, agregar cada archivo a filesToTest
                            filesToTest.addAll(filePaths)
                        } else {
                            // Si no es una lista, agregar el único archivo directamente
                            filesToTest.add(filePaths)
                        }
                    }
                }

                echo "Files to test: ${filesToTest}"

                // Si 'filesToTest' tiene más de un archivo, unir los valores con un espacio
                if (filesToTest.size() > 0) {
                    filesToTest = filesToTest.join(' ')
                } else {
                    echo "No files found for the given LABEL_SCENARIO"
                }

                echo "Final files to test: ${filesToTest}"


                 sh """
                        . venv/bin/activate
                        pytest $filesToTest -m ${params.LABEL_SCENARIO} -v --alluredir=target/allure-results --log-cli-level=${params.LOG_LEVEL}
                    """
                }
            }
        }
    }

post {
    always {
        script {
        def n8nWebhookUrl = 'https://n8n.subocol.com/webhook-test/39b741fd-57b5-410b-b8ba-9bd3a0754dad' // ¡IMPORTANTE: Reemplaza con tu URL real de n8n!

                // Construye el payload JSON con la información del build
                 def payloadMap = [
                    jobName: env.JOB_NAME,
                    buildNumber: env.BUILD_NUMBER,
                    buildUrl: env.BUILD_URL,
                    buildStatus: currentBuild.result,
                    allureReportUrl: "${env.BUILD_URL}/allure/"
                ]

                // Convierte el mapa Groovy a una cadena JSON
                def jsonPayload = JsonOutput.toJson(payloadMap)

                echo "Sending webhook to n8n via curl to: ${n8nWebhookUrl}"
                try {
                    // Enviar la solicitud HTTP POST usando curl
                    sh """
                        curl -X POST \\
                             -H "Content-Type: application/json" \\
                             -H "X-Jenkins-Event: build_finished" \\
                             -d '${jsonPayload}' \\
                             "${n8nWebhookUrl}"
                    """
                    echo "Webhook sent successfully to n8n using curl."
                } catch (Exception e) {
                    echo "WARNING: Failed to send webhook to n8n via curl. Error: ${e.getMessage()}"
                    // No falles el pipeline solo porque el webhook falló
                }

        echo 'Processing Allure results for failed tests...'
                    def failedTestsJson = []
                    def allureResultsDir = 'target/allure-results' // Asegúrate de que esta ruta es correcta

                    // Asegúrate de que el directorio 'allure-results' existe y contiene archivos.
                    def resultFiles = findFiles(glob: "${allureResultsDir}/*-result.json")

                    if (resultFiles.length == 0) {
                        echo "No Allure result files found in ${allureResultsDir}. Skipping failed test summary generation."
                    } else {
                        resultFiles.each { f ->
                            def fileContent = readFile file: f.path
                            def testResult = readJSON text: fileContent

                            if (testResult.status == 'failed' || testResult.status == 'broken') {
                                failedTestsJson.add([
                                    name: testResult.name,
                                    fullName: testResult.fullName,
                                    status: testResult.status,
                                    message: testResult.statusDetails?.message,
                                    stackTrace: testResult.statusDetails?.trace,
                                    uuid: testResult.uuid,
                                    jobName: env.JOB_NAME, // Propaga env vars para usar en el summary.json
                                    buildNumber: env.BUILD_NUMBER,
                                    buildUrl: env.BUILD_URL,
                                    allureReportUrlBase: "https://jenkins.subocol.com/job/${env.JOB_NAME}/${env.BUILD_NUMBER}/allure/"
                                ])
                            }
                        }

                        if (!failedTestsJson.isEmpty()) {
                            writeJSON file: 'failed_tests_summary.json', json: failedTestsJson
                            echo "Generated failed_tests_summary.json with ${failedTestsJson.size()} failed tests."
                            archiveArtifacts artifacts: 'failed_tests_summary.json', fingerprint: true
                        } else {
                            echo "No failed or broken tests found. Skipping failed_tests_summary.json generation."
                        }
                    }
            if (params.CHANGE_MOCK_VARIABLES == 'SI') {
                sh '''
                    . venv/bin/activate
                    python -c "from src.orbika.facts.aws.fact_conditions_test_aws import FactConditionsTestsAws; FactConditionsTestsAws().fact_change_lambda_params('cognito', True)"
                '''
            }
            allure includeProperties: false, jdk: '', results: [[path: 'target/allure-results']]
            archiveArtifacts artifacts: 'failed_tests_summary.json', fingerprint: true
            def allureReportUrl = "https://jenkins.subocol.com/job/${pipelineName}/${env.BUILD_NUMBER}/allure/"
            env.ALLURE_URL = allureReportUrl
        }

         script {
             withCredentials([
                 string(credentialsId: 'telegram_qa_bot_token', variable: 'TELEGRAM_BOT_TOKEN'),
                 string(credentialsId: 'telegram_qa_chat_id', variable: 'TELEGRAM_CHAT_ID')
             ]) {
                 def message = "⌛️⌛️ Ejecución Nro: ${env.BUILD_NUMBER} finalizada para la funcionalidad ${params.FUNCTIONALITY} en el ambiente ${params.ENVIRONMENT} ⌛️⌛️️‍."
                 sendTelegramMessage(message)
             }
         }
    }

     success {
         script {
             withCredentials([
                 string(credentialsId: 'telegram_qa_bot_token', variable: 'TELEGRAM_BOT_TOKEN'),
                 string(credentialsId: 'telegram_qa_chat_id', variable: 'TELEGRAM_CHAT_ID')
             ]) {
                 def message = "✅ Ejecución de pruebas exitosas para la funcionalidad ${params.FUNCTIONALITY} en el ambiente ${params.ENVIRONMENT}, validar reporte ${env.ALLURE_URL} ✅"
                 sendTelegramMessage(message)
             }
         }
     }

     failure {
         script {
             withCredentials([
                 string(credentialsId: 'telegram_qa_bot_token', variable: 'TELEGRAM_BOT_TOKEN'),
                 string(credentialsId: 'telegram_qa_chat_id', variable: 'TELEGRAM_CHAT_ID')
             ]) {
                 def message = "❌ Ejecución de pruebas fallidas para la funcionalidad ${params.FUNCTIONALITY} en el ambiente ${params.ENVIRONMENT}, validar reporte ${env.ALLURE_URL} ❌"
                 sendTelegramMessage(message)
             }
         }
     }
 }
}


 def sendTelegramMessage(String message) {
     env.message_send = message
     def curlResult = sh(script: '''
          bash send_telegram_notification.sh $TELEGRAM_BOT_TOKEN $TELEGRAM_CHAT_ID \"$message_send\"
     ''', returnStatus: true)

     if (curlResult != 0) {
         echo "Error al enviar mensaje de Telegram. Código de salida: ${curlResult}"

         }
     }