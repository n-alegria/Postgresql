import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='localhost',
                            port='5432',
                            database='test_db'
                            )



# Auto-commit (guarda la informacion en la base de datos)
# Con esto no sera necesario hacer el commit a la base de datos, se realiza automaticamente
conexion.autocommit = True

cursor = conexion.cursor()
sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'

# Debo crear una tupla con los valores a insertar
valores = ('Josefa','Zaf','jz@mail.com')

# Le paso la tupla a la consulta
cursor.execute(sentencia, valores)

# Para saber si hubo filas modificadas puedo  usar 'cursor.rowcont' lo cual me dira la cantidad de filas modificadas
registros_insertados = cursor.rowcount
print(f'Registros insertados: {registros_insertados}')

cursor.close()
conexion.close()