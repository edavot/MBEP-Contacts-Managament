""" User.py """
import file

class Contact:
    
    FILE_NAME = 'contacts.json'

    nombre: str
    apellido: str
    telefono: str
    correo_electronico: str
    calle: str
    num_ext: str
    num_int: str
    colonia: str
    municipio_alcadia: str
    ciudad: str
    estado: str
    pais: str

    def __init__(self, nombre: str, apellido: str, telefono: str, correo_electronico:str, calle: str, num_ext: str, colonia: str, municipio_alcadia: str, 
                 ciudad: str, estado: str, pais: str, num_int: str = ''):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo_electronico = correo_electronico
        self.calle = calle
        self.num_ext = num_ext
        self.num_int = num_int
        self.colonia  = colonia
        self.municipio_alcadia  = municipio_alcadia
        self.ciudad = ciudad
        self.estado = estado
        self.pais = pais
        
    def save(self):
        file.create_or_update(self.FILE_NAME, self.__dict__)


# test = Contact('Enrique', 'Avalos','5512345678','avalosenator@gmail.com','AV FF CC', '1234', 'Bondojito','Gustavo A. Madero', 'CDMX', 'CDMX', 'México')
# test.save()
