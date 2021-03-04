import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='localhost',
                            port='5432',
                            database='test_db'
                            )

cursor = conexion.cursor()
sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'

# Debo crear cada una tupla con los datos a mdificar y el id de esa persona
valores = ('Carla','Perez','cp@mail.com', 1)

# Ejecuto la consulta con 'execute'
cursor.execute(sentencia, valores)

# Es necesario guardar la informacion luego de la sentencia
# Esto se logra haciendo un 'commit' a la conexion, son necesarias para 'insert', 'update' y 'delete'
conexion.commit()

# Para saber si hubo filas modificadas puedo  usar 'cursor.rowcont' lo cual me dira la cantidad de filas modificadas
registros_insertados = cursor.rowcount
print(f'Registros actualizados: {registros_insertados}')

cursor.close()
conexion.close()