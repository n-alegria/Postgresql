import logging

logger = logging
# Modifico el nivel de visibilidad, por default de Waring hacia abajo, con esto veo desde dEBUG
logger.basicConfig(
    level = logging.DEBUG,
    # Con esto configuro el mensaje a mostrar cuando se ejecuta el logger
    # (hora, nivel en el cual se ejecuto el logger, de que archivo y linea se envia el mensaje, y el mensaje)
    format = '%(asctime)s: %(levelname)s [%(filename)s]: %(lineno)s - %(message)s',
    # Configuro el formato de la hora, tambien podria incluir la fecha
    datefmt = '%I:%M:%S %p',
    handlers = [
        logging.FileHandler('capa_datos.log'),
        logging.StreamHandler()
    ]
)

# Handlers
'''
Con los Handlers manejo la informacion del logger, con 'FileHandler' le indico que se todo lo que se
imprima en consola se almacene enla variable 'capa_datos.log' y con 'StreamHandler' que se imprima 
en la consola
'''

# El condicional sirve para que solo se ejecute si se lanza desde este archivo
# Si importo el modulo no se ejecuta ya que deja de ser el main
if __name__ == '__main__':
    logger.warning('mensaje a nivel de warning')
    logger.info('mensaje a nivel de info')
    logger.debug('mensaje a nivel de debug')
    logger.error('Ocurrio un error en la base de datos')
    logger.warning('Se realizo la conexion con exito')