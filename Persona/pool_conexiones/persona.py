from logger_base import logger

class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None):
        self.__id_persona = id_persona
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
    
    def __str__(self):
        return (f'Id Persona: {self.__id_persona} - Nombre: {self.__nombre} - Apellido: {self.__apellido} - Email: {self.__email}')
        
    def get_id(self):
        return self.__id_persona    
    
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_email(self):
        return self.__email
        
if __name__ == '__main__':
    persona = Persona(1, 'lautaro', 'fernandez', 'email')
    logger.debug(persona)