import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='localhost',
                            port='5432',
                            database='test_db'
                            )

cursor = conexion.cursor()
sql = 'SELECT * FROM persona ORDER BY id_persona'
cursor.execute(sql)
registros = cursor.fetchall()
for registro in registros:
    print(registro[1])


cursor.close()
conexion.close()
