""" main.py """
from Contact import Contact

print("#### Libreta de direcciones #### ")

def show_menu():
    """Show menu"""
    valid_option = False
    options = ["1", "2", "3", "4", "5", "6"]

    print("\n 1) Agregar contacto ")
    print(" 2) Consultar contacto ")
    print(" 3) Eliminar contacto ")
    print(" 4) Listado de contactos ")
    print(" 5) Numero de contactos")
    print(" 6) Mostrar parte de la lista de contactos \n")

    while not valid_option:
        option = input("Selccione la opción: ")
        valid_option = option in options
        if valid_option:
            select_option(option)

def select_option(option: str):
    """Select options

    Args:
        option (str): Option selected
    """
    if option == "1":
        add_contact()
    elif option == "2":
        search_contact()
    elif option == "3":
        delete_contact()
    elif option == "4":
        list_contacts()
    elif option == "5":
        count_contacts()
    elif option == "6":
        slice_contacts()
    return_menu()

def add_contact():
    """Add contact"""
    nombre = input_message("Ingresa el nombre: ")
    apellido = input_message("Ingresa el apellido: ")
    telefono = input_message("Ingresa el telefono: ")
    correo_electronico = input_message("Ingresa el correo electronico: ")
    calle = input_message("Ingresa la calle: ")
    num_ext = input_message("Ingresa el numero exterior: ")
    num_int = input_message("Ingresa el numero interior (opcional): ", False)
    colonia = input_message("Ingresa la colonia: ")
    municipio_alcadia = input_message("Ingresa el municipio/alcadia: ")
    ciudad = input_message("Ingresa la ciudad: ")
    estado = input_message("Ingresa el estado: ")
    pais = input_message("Ingresa el pais: ")
    id_contact = Contact(
        nombre,
        apellido,
        telefono,
        correo_electronico,
        calle,
        num_ext,
        colonia,
        municipio_alcadia,
        ciudad,
        estado,
        pais,
        num_int,
    ).save()
    print(f'Se agrego el contacto: {id_contact}')

def search_contact():
    """Search contact"""
    email = input_message("Ingresa el correo a buscar: ")
    contact = Contact("", "", "", "", "", "", "", "", "", "", "").search(email)
    if len(contact) == 0:
        print('No se encontraron coincidencias con los datos ingresados')
        return
    print(contact)

def delete_contact():
    """Delete contact"""
    email = input_message("Ingresa el correo a eliminar: ")
    Contact('', '', '', '', '', '', '', '', '', '', '').delete(email)

def list_contacts():
    """List of contacts"""
    print(f" \n{Contact('','','','','','','','','','','').get_all()}")

def count_contacts():
    """Number of contacts"""
    print(
        f" \nNumero de contactos: {Contact('','','','','','','','','','','').count()}"
    )

def slice_contacts():
    """Number of contacts"""
    lenght = ''
    while not lenght.isnumeric():
        lenght = input_message("Ingresa el numero de contactos a mostrar: ")
    print(f" \n{Contact('','','','','','','','','','','').slice(int(lenght))}")

def return_menu():
    """Return to principal menu"""
    valid_option = False
    options = ["Y", "N", "S", "YES", "NO", "SI"]
    while not valid_option:
        option = input(" \n ¿Deseas realizar otra operación? (Y/N)").upper()[0:1]
        valid_option = option in options
        if valid_option and (option == "Y" or option == "S"):
            show_menu()

def input_message(message: str, required: bool = True) -> str:
    """Input messaga to user

    Args:
        message (str): Message to show
        required (bool, optional): Input value is required. Defaults to True.
    """
    value = ""
    if required:
        while len(value) == 0:
            value = input(message)
    else:
        value = input(message)
    return value

show_menu()
