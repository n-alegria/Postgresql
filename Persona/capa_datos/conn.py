import  psycopg2

credenciales = {
        "dbname": "test_db",
        "user": "postgre",
        "password": "admin",
        "host": "localhost",
        "port": '5432'
    }

conexion = psycopg2.connect(credenciales)

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