Este proyecto tiene el código de una función que extrae el texto de una 
factura en formato imagen y lo pasa a chatgpt para extraer datos contables de la factura.


La función se prueba en modo local con:
make local-build-run

Previamente es necesario crear el dev.env con la variable de entorno del token chatgpt y crear el firebase.json para comunicarse con la base de datos de firebase.

La función se deploya con:
make prod-deploy

Previamente es necesario crear el firebase.json para comunicarse con la base de datos de firebase.

La función se prueba con: 
make prod-test