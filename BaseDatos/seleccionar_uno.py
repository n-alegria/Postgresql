import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='localhost',
                            port='5432',
                            database='test_db'
                            )

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona WHERE id_persona = %s'

# Puedo reemplazar por parametros, para ello debo utilizar una tupla
id_persona = input('Ingresa el pk a buscar: ')
llave_primaria = tuple(id_persona) # O aplico una coma luego de la variable (id_persona, )

# Ahora se lo paso por parametro a la consulta
cursor.execute(sentencia, llave_primaria)
registros = cursor.fetchone()
print(registros)


cursor.close()
conexion.close()