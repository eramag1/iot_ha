1.- Instalar node

2.- Instalar el modulo node de swagger para locust

	npm install swagger-to-locustfile

3.- Ejecutar el fichero swagger2locust .js que genera las task de locust a partir de la especificación swagger

node swagger2locust /path/to/swagger.json  > /tmp/locustfile.py