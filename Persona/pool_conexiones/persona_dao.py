from persona import Persona
from cursor_del_pool import CursorDelPool
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
        # Abre el cursor y lo cierra de manera automatica
        # Manda a llamar la obtencion del cursor, llama a dos metodos que de manera automatica inicia el cursor y luego lo elimina (__enter__ y __exit__) 
        with CursorDelPool() as cursor:
            # Podemos mandar a la consola el Query que se va a ejecutar, no el que escribimos sino el compilado
            logger.debug(cursor.mogrify(cls.__SELECCIONAR))
            cursor.execute(cls.__SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas
    
    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Persona a insertar: {persona}')
            valores = (persona.get_nombre(), persona.get_apellido(), persona.get_email())
            cursor.execute(cls.__INSERTAR, valores)
            return cursor.rowcount
            
    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Persona a actualizar: {persona}')
            valores = (persona.get_nombre(), persona.get_apellido(), persona.get_email(), persona.get_id())
            cursor.execute(cls.__ACTUALIZAR, valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f'Persona a eliminar: {persona}')
            valores = (persona.get_id(),)
            cursor.execute(cls.__ELIMINAR, valores)
            return cursor.rowcount
    
    
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
    
    