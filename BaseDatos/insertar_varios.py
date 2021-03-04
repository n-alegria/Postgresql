import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='localhost',
                            port='5432',
                            database='test_db'
                            )

cursor = conexion.cursor()
sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'

# Debo crear cada una de las tuplas de los registros a insertar
valores = (
    ('Juan','Chal','sd@mail.com'),
    ('Ana', 'Sanchez', 'as@mail.com')
)

# Como son varios registros a insertar debo utilizar 'executemany'
cursor.executemany(sentencia, valores)

# Es necesario guardar la informacion luego de la sentencia
# Esto se logra haciendo un 'commit' a la conexion, son necesarias para 'insert', 'update' y 'delete'
conexion.commit()

# Para saber si hubo filas modificadas puedo  usar 'cursor.rowcont' lo cual me dira la cantidad de filas modificadas
registros_insertados = cursor.rowcount
print(f'Registros insertados: {registros_insertados}')

cursor.close()
conexion.close()