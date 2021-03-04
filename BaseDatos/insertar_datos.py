import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='localhost',
                            port='5432',
                            database='test_db'
                            )

cursor = conexion.cursor()
sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'

# Debo crear una tupla con los valores a insertar
valores = ('Sebastian','Dominguez','sd@mail.com')

# Le paso la tupla a la consulta
cursor.execute(sentencia, valores)

# Es necesario guardar la informacion luego de la sentencia
# Esto se logra haciendo un 'commit' a la conexion, son necesarias para 'insert', 'update' y 'delete'
conexion.commit()

# Para saber si hubo filas modificadas puedo  usar 'cursor.rowcont' lo cual me dira la cantidad de filas modificadas
registros_insertados = cursor.rowcount
print(f'Registros insertados: {registros_insertados}')

cursor.close()
conexion.close()