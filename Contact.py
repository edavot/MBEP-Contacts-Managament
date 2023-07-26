""" Contact.py """
import file

class Contact:
    """Class representing a contact"""
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

    def __init__(
        self,
        nombre: str,
        apellido: str,
        telefono: str,
        correo_electronico:str,
        calle: str,
        num_ext: str,
        colonia: str,
        municipio_alcadia: str,
        ciudad: str,
        estado: str,
        pais: str,
        num_int: str = ''
    ):
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

    def save(self) -> str:
        """Save a contact
        """
        file.create_or_update(self.FILE_NAME, self.__dict__)

    def get_all(self) -> list:
        """Get all list of contacts 
        """
        content = file.read(self.FILE_NAME)
        contacts = [ content ] if isinstance(content, dict) else content
        return contacts

    def count(self):
        """Get number of contacts 
        """
        return len(self.get_all())

    def search(self, value:str) -> list:
        """Search a contact by email

        Args:
            value (str): email to find
        """
        return [
            contact
            for contact in self.get_all()
            if contact['correo_electronico'] == value
        ]

    def delete(self, value: str):
        """Delete a contact by email

        Args:
            value (str): email to delete
        """
        file.replace(self.FILE_NAME, [
            contact
            for contact in  self.get_all()
            if contact['correo_electronico'] != value
        ])

    def slice(self, lenght: int)  -> list:
        """Slice of list of contacts

        Args:
            lenght (int): email to delete
        """
        return self.get_all()[0:lenght]
