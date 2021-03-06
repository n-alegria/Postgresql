from conexion import Conexion
from logger_base import logger

class CursorDelPool:
    def __init__(self):
        self.__conn = None
        self.__cursor = None
        
    # Inicio del 'with'
    def __enter__(self):
        # El metodo crea el pool de conexiones, en caso de existir obtiene una conexion del pool
        logger.debug('Inicio de with método __enter__')
        self.__conn = Conexion.obtenerConexion()
        self.__cursor = self.__conn.cursor()
        return self.__cursor # Retornamos el cursor
        
    # Fin del 'with'
    def __exit__(self, exception_type, exception_value, exception_traceback):
        # Ejecuta un 'rollback' si hubo un error o un commit si no hubo error
        # Al final cierra el cursor y libera las conexiones
        logger.debug(f'Se ejecuta metodo __exit__()')
        if exception_value: # Or -> if exception_value is not None:
            self.__coon.rollback()
            logger.debub(f'Ocurrio una excepcion: {exception_value}')
        else:
            self.__conn.commit()
            logger.debug(f'Commit de la transaccion')
        # Cerramos el cursor 
        self.__cursor.close()
        # Regresar la conexion al pool
        Conexion.liberarConexion(self.__conn)
        
if __name__ == '__main__':
    # Obtener un cursor a partir de la conexion del pool
    # Con with se ejecuta primero el metodo '__enter__' y termina con '__exit__'
    with CursorDelPool() as cursor: # llama de manera automatica el metodo '__enter__' lo cual retorna un cursor de la conexion
        cursor.execute('SELECT * FROM persona')
        logger.debug('Listado de personas')
        logger.debug(cursor.fetchall())