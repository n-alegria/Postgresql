from logger_base import logger
import psycopg2
import sys

class Conexion:
    __DATABASE = 'test_db'
    __USERNAME = 'postgres'
    __PASSWORD = 'admin'
    __DB_PORT = '5432'
    __HOST = '127.0.0.1'
    __conexion = None
    __cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls.__conexion is None:
            try:
                cls.__conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='localhost',
                            port='5432',
                            database='test_db'
                            )
                logger.debug(f'Conexion exitosa: {cls.conexion}')
                return cls.__conexion
            except Exception as e:
                logger.error(f'Error al conectar a la BD: {e}')
                sys.exit()
        else:
            return cls.__conexion

if __name__ == '__main__':
    logger.info(Conexion.obtenerConexion())