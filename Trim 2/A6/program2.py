import sys

def m():
    phone_book = {}
    while True:

        print('''
        1. Mostrar lista de contactos.
        2. Añadir contacto (nombre y teléfono).
        3. Borrar contacto (nombre).
        4. Salir.
        ''')

        m = input("¿Qué quieres hacer?: ")

        if m == '1':
            show_contacts(phone_book)


        elif m == '2':
            name = input("Nombre del contacto que quieres agregar: ")
            if name not in phone_book:
                phone = input("Número de teléfono de telefono del contacto que vas a agregar: ")
                add_contact(phone_book, name, phone)
            else:
                print("Ha sido agregado con exito. ")


        elif m == '3':
            name = input("Nombre del contacto que quieres eliminar: ")
            if name in phone_book:
                remove_contact(phone_book, name)
            else:
                print("El contacto que quieres eliminar no esta en la lista de contactos. ")

        elif m == '4':
            break

        elif m > '4':
            print("Elige una opción válida: ")

def show_contacts(phone_book):
    if phone_book == {}:
        print("La agenda está vacía. Por favor, añade contactos para poder usar el menú.")
    else:
        for name, phone in phone_book.items():
            print(name, ":", phone)

def add_contact(phone_book, name, phone):
    phone_book[name] = phone

def remove_contact(phone_book, name):
    del(phone_book[name])

if __name__ == '__main__':
    m()