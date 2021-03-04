import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='localhost',
                            port='5432',
                            database='test_db'
                            )

cursor = conexion.cursor()
# El operador 'IN' nos permite proporcionar varios valores, en este caso la llave primaria
sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'

# Reemplazo el comodin por cada valor en la tupla, para ello debo crear una tupla de tuplas
#llaves_primarias = ((1, 2, 3), )

entrada = input('Proporciona las pk, a buscar (separadas por comas): ')
tupla = tuple(entrada.split(',')) # separa los elementos donde encuentre una coma
llaves_primaria = (tupla, ) # Creo la tupla de tuplas

# Ahora se lo paso por parametro a la consulta
cursor.execute(sentencia, llaves_primaria)
registros = cursor.fetchall()
print(registros, '\n')

# Imprimo todos de forma individual
for registro in registros:
    print(registro)

cursor.close()
conexion.close()