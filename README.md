# sbc-automation-py-qa-template
template para pruebas automatizadas backend en python

# Estructura arbol carpeta src/orbika
# conf
Permite realizar las configuraciones de proyecto (ulr, constantes, etc)

# endpoints
Se gestionan las peticiones a los diferentes servicio

# enums
Variables con valores inmutables que se llaman en codigo que poseen valores fijos y nombres descriptivos (ejemplo: insurer: 500000002: nombre: sura colombia)

# exceptions
Clases que controlan las excepciones retornadas por los servicios utilizados

# factories
Clases que permiten obtener el dato especifico del banco de datos alojado en resources/data/{ambiente} datos previamente definidos en el cual el cambio de un valor habilita un escenario de prueba

# facts
Permite definir las precondiciones necesarias para ejecutar la prueba

# features
Clase donde se definene las pruebas a realizar a nivel de negocio o a nivel de base de datos

# models
Clases donde se define la representación estructurada de las respuestas esperadas en los servicios.
Cada modelo describe los campos y validaciones necesarias para asegurar que las respuestas de las APIs
cumplan con el formato y los datos esperados, simplificando la validación y mejorando la legibilidad del código.

# tasks
Clases que permiten realizar las tareas necesarias para definir los pasos de la prueba

# util
Funciones transversales al proyecto
