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
        # Si la conexion no existe la crea
        if cls.__conexion is None:
            try:
                cls.__conexion = psycopg2.connect(host=cls.__HOST,
                                                  user=cls.__USERNAME,
                                                  password=cls.__PASSWORD,
                                                  port=cls.__DB_PORT,
                                                  database=cls.__DATABASE
                )
                # Enviamos un mensaje a nivel Debug
                logger.debug(f'Conexion exitosa: {cls.__conexion}')
                # Devuelve el objeto conexion
                return cls.__conexion
            except Exception as e:
                # Si no se pudo conectar envia un error a nivel Error y cierra la aplicacion
                logger.error(f'Error al conectar a la BD: {e}')
                sys.exit()
        # Si ya fue iniciado previamente lo retorna
        else:
            return cls.__conexion

    @classmethod
    def obtenerCursor(cls):
        if cls.__cursor is None:
            try:
                # Asigna a la variable el cursor que obtengo del llamado al metodo, este metodo tiene la conexion
                cls.__cursor = cls.obtenerConexion().cursor()
                logger.debug(f'Se abrio el cursor con exito: {cls.__cursor}')
                return cls.__cursor
            except Exception as e:
                logger.error(f'Error al obtener el cursor: {e}')
                sys.exit()
        else:
            return cls.__cursor

    @classmethod
    def cerrar(cls):
        if cls.__cursor is not None:
            try:
                cls.__cursor.close()
            except Exception as e:
                logger.error(f'Error al cerrar cursor: {e}')
        if cls.__conexion is not None:
            try:
                cls.__conexion.close()
            except Exception as e:
                logger.error(f'Error al cerrar la conexion: {e}')
        logger.debug('Se han cerrado los objetos.')

if __name__ == '__main__':
    logger.info(Conexion.obtenerCursor())
    Conexion.cerrar()