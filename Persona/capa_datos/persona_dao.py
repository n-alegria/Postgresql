from persona import Persona
from conexion import Conexion
from logger_base import logger

class PersonaDao:
    '''
    DAO (Data Access Object)
    CRUD: Create-Read-Update-Delete sobre la entidad Persona
    '''
    __SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    __INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s,%s,%s)'
    __ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona = %s'
    __ELIMINAR = 'DELETE FROM persona WHERE id_persona = %s'
    
    @classmethod
    def seleccionar(cls):
        cursor = Conexion.obtenerCursor()
        # Podemos mandar a la consola el Query que se va a ejecutar, no el que escribimos sino el compilado
        logger.debug(cursor.mogrify(cls.__SELECCIONAR))
        cursor.execute(cls.__SELECCIONAR)
        registros = cursor.fetchall()
        personas = []
        for registro in registros:
            persona = Persona(registro[0], registro[1], registro[2], registro[3])
            personas.append(persona)
        Conexion.cerrar()
        return personas
    
    @classmethod
    def insertar(cls, persona):
        try:
            cursor = Conexion.obtenerCursor()
            conexion = Conexion.obtenerConexion()
            
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Persona a insertar: {persona}')
            
            valores = (persona.get_nombre(), persona.get_apellido(), persona.get_email())
            
            cursor.execute(cls.__INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
            
        except Exception as e:
            # Con 'rollback' doy marcha atras a cualquier cambio que se efectuo a la base de datos
            conexion.rollback()
            logger.error(f'Error al insertar persona: {e}')
            
        finally:
            Conexion.cerrar()
            
    @classmethod
    def actualizar(cls, persona):
        try:
            cursor = Conexion.obtenerCursor()
            conexion = Conexion.obtenerConexion()
            
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Persona a actualizar: {persona}')
            
            valores = (persona.get_nombre(), persona.get_apellido(), persona.get_email(), persona.get_id())
            
            cursor.execute(cls.__ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
            
        except Exception as e:
            # Con 'rollback' doy marcha atras a cualquier cambio que se efectuo a la base de datos
            conexion.rollback()
            logger.error(f'Error al actualizar persona: {e}')
            
        finally:
            Conexion.cerrar()
    
    @classmethod
    def eliminar(cls, persona):
        try:
            cursor = Conexion.obtenerCursor()
            conexion = Conexion.obtenerConexion()
            
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f'Persona a eliminar: {persona}')
            
            valores = (persona.get_id(),)
            
            cursor.execute(cls.__ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
            
        except Exception as e:
            # Con 'rollback' doy marcha atras a cualquier cambio que se efectuo a la base de datos
            conexion.rollback()
            logger.error(f'Error al eliminar persona: {e}')
            
        finally:
            Conexion.cerrar()
    
    
    
if __name__ == '__main__':
    personas = PersonaDao.seleccionar()
    for persona in personas:
        logger.debug(persona)
    
    # persona = Persona(nombre='Javier', apellido='Sanchez', email='jz@mail.com')
    # personas_insertadas = PersonaDao.insertar(persona)
    # logger.debug(f'Registros insertados: {personas_insertadas}')
    
    # persona = Persona(id_persona=3, nombre='Jorge', apellido='Sanchez', email='jz@mail.com')
    # persona_modificada = PersonaDao.actualizar(persona)
    # logger.debug(f'Registros insertados: {persona_modificada}')
    
    # persona = Persona(id_persona=1)
    # persona_eliminada = PersonaDao.eliminar(persona)
    # logger.debug(f'Registros insertados: {persona_eliminada}')
    
    