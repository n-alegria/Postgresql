from logger_base import logger
import psycopg2
import sys

class Conexion:
    __DATABASE = 'test_db'
    __USERNAME = 'postgres'
    __PASSWORD = 'admin'
    __DB_PORT = '5432'
    __HOST = 'localhost'
    __conexion = None
    __cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls.__conexion is None:
            try:
                cls.__conexion = psycopg2.connect(host=cls.__HOST,
                                                  user=cls.__USERNAME,
                                                  password=cls.__PASSWORD,
                                                  port=cls.__DB_PORT,
                                                  database=cls.__DATABASE
                            )
                logger.debug(f'Conexion exitosa: {cls.__conexion}')
                return cls.__conexion
            except Exception as e:
                logger.error(f'Error al conectar a la BD: {e}')
                sys.exit()
        else:
            return cls.__conexion

if __name__ == '__main__':
    logger.info(Conexion.obtenerConexion())