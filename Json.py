import json
'''

contactos = {
    "nombre":"Marco",
    "telefono": 2283110731,
    "correo e.":"ejemplo@hotmail.com",
    "direccion":"Santa Maria"
}
#forma de escritura
with open("contactos.json","w") as outfile:
    json.dump(contactos,outfile,indent=4)
#forma de lectura
with open("contactos.json") as file:
    data = json.load(file)    
print(data)

'''
#funcion para leer contactos
def leer(nombre):
    try:
        with open(nombre,"r") as file:
            return json.load(file)
        #si el archivo no existe o no se encontro retornar lista vacia para agregar elementos
    except FileNotFoundError as fe:
        print("Error: Archivo no Encontrado, Creando Archivo ",fe)
        return []
    except json.JSONDecodeError:
        print("Error al decodificar archivo .JSON ")
        return []    

def guardar(nombre,contactos):
    try:
        with open(nombre,"w") as file:
            json.dump(contactos,file,indent=4)
    except IOError as io:
        print("Error al escribir en el Archivo!! ",io)    

def mostrar(contactos):
    for contacto in contactos:
        print("*" * 20)
        print(f"Nombre: {contacto["Nombre"]}")
        print(f"Telefono: {contacto["Telefono"]}")
        print(f"Correo: {contacto["Correo"]}")
        print(f"Direccion: {contacto["Direccion"]}")   
        print("*" * 20)

def agregar(contactos):
    nombre = input("Ingresa un nombre: ")
    telefono = int(input("Ingresa un Numero Telefonico: "))
    correo = input("Ingresa un correo electronico: ")
    direccion = input("Ingresa una Direccion: ")
    nuevo_contacto = {
        "Nombre":nombre,
        "Telefono":telefono,
        "Correo":correo,
        "Direccion":direccion
    }
    contactos.append(nuevo_contacto)
    return contactos

def buscar(contactos,nombre_buscar):
    for contacto in contactos:
        if contacto["Nombre"].lower() == nombre_buscar.lower():
            return contacto
    return None    

def eliminar(contactos,nombre_eliminar):
    for i,contacto in enumerate(contactos):
        if contacto["Nombre"].lower() == nombre_eliminar.lower():
            del contacto[i]
            return contactos
    return None    

def gestionar():
    nombre = "contactos.json"
    contactos = leer(nombre)

    while True:
        print("\n**** Menu ****")
        print("1- Mostrar Contactos")
        print("2- Agregar Contacto")
        print("3- Buscar Contacto por Nombre")
        print("4- Eliminar Contacto")
        print("5- Salir!")
        opc = int(input("Selecciona una Opcion Valida: "))
        if opc == 1:
            mostrar(contactos)
        elif opc == 2:
            contactos = agregar(contactos) 
            guardar(nombre,contactos)
        elif opc == 3:
            nombre_buscar = input("Ingresa el Nombre del contacto a Buscar: ")
            contacto = buscar(contactos,nombre_buscar)
            if contacto:
                print("*" * 20)
                print(f"Nombre: {contacto["Nombre"]}")
                print(f"Telefono: {contacto["Telefono"]}")
                print(f"Correo: {contacto["Correo"]}")
                print(f"Direccion: {contacto["Direccion"]}")   
                print("*" * 20)
            else:
                print("Contacto no Encontrado")
            
        elif opc == 4:
            nombre_eliminar = input("Ingresa el nombre del contacto a Eliminar: ")
            contactos_actualizados = eliminar(contactos,nombre_eliminar)
            if contactos_actualizados is not None:
                contactos = contactos_actualizados
                guardar(nombre,contactos)
                print("Contacto Eliminado Exitosamente")
            else:
                print("Contacto no existe...")    
        elif opc == 5:
            print("Cerrando Gestor de Contactos...")
            print("*" * 20)
            break
        else:
            print("Opcion Invalida, intente de nuevo")    

gestionar()                




