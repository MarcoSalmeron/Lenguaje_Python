#gestionar una biblioteca
#funcion: leer,mostrar,agregar,buscar

import json
from collections import defaultdict

#funcion para leer y mostrar datos
def leer_datos(nombre_archivo):
    try:
        with open(nombre_archivo,"r") as File:
            #leer el archivo
            return json.load(File)
    except FileNotFoundError:
        print("Archivo no Encontrado...")
        return []
    except json.JSONDecodeError:
        print("Error al decodificar Archivo .json")
        return []    
#mostrar datos
def mostrar_datos(nombre_archivo):
    for datos in nombre_archivo:
        #metodo para leer los datos
        print(json.dumps(datos,indent=4))

#guardar datos
def guardar_datos(datos,nombre_archivo):
    try:
        with open(nombre_archivo,"a") as File:
            json.dump(datos,File,indent=4)
    except Exception as ex:
        print("Error al guardar en: ",nombre_archivo,ex)

#agregar libros
def agregar_libro(libros):
    id_libro = input("ID del Libro: ")
    titulo = input("Titulo del Libro: ")
    autor = input("Autor del Libro: ")
    categoria = input("Categoria del Libro: ")

    nuevo_libro = {
        "ID_libro":id_libro,
        "Titulo":titulo,
        "Autor":autor,
        "Categoria":categoria,
        "Disponible":True
    }
    libros.append(nuevo_libro)
    guardar_datos(libros,"libros.json")

#agregar miembros
def agregar_miembro(miembros):
    id_miembro = input("ID de Miembro: ")
    nombre_miembro = input("Nombre del Miembro: ")
    email = input("Email del Miembro: ")

    nuevo_miembro = {
        "ID_miembro":id_miembro,
        "Nombre":nombre_miembro,
        "Email":email
    }
    miembros.append(nuevo_miembro)
    guardar_datos(miembros,"miembros.json")

#buscar libro por titulo o id
def buscar_libro(libros):
    criterio = input("Buscar por (1) ID o (2) Titulo: ")
    valor = input("Ingresa el valor de busqueda: ")

    for libro in libros:
        if (criterio == "1" and libro["ID_libro"] == valor) or (criterio == "2" and libro["Titulo"] == valor):
            print(json.dumps(libro,indent=4))
            return libro
    print("Libro no Encontrado...")
    return None

#listar libros
def listar_libros(libros):
    for libro in libros:
        print(libro)

#listar miembros
def listar_miembros(miembros):
    for miembro in miembros:
        print(miembro)

#listar prestamos
def listar_prestamos(prestamos):
    for prestamo in prestamos:
        print(prestamo)

#buscar miembro por nombre o id
def buscar_miembro(miembros):
    criterio = input("Buscar por (1) ID o (2) Nombre: ")
    valor = input("Ingresa el valor de busqueda: ")
    for miembro in miembros:
       if (criterio == "1" and miembro["ID_miembro"] == valor) or (criterio == "2" and miembro["Nombre"] == valor):
           print(json.dumps(miembro,indent=4))
           return miembro
    print("Miembro no Encontrado...")
    return None

#prestamos
def prestar_libro(libros,miembros,prestamos):
    id_libro = input("Ingresa el ID del libro a emitir: ")
    id_miembro = input("Ingresa el ID del miembro: ")

    libro = None
    for lib in libros:
        if lib["ID_libro"] == id_libro:
            libro = lib
            break
    if libro is None or not libro["Disponible"]:
        print("Libro no Disponible o Inexistente")
        return
    
    miembro = None
    for miemb in miembros:
        if miemb["ID_miembro"] == id_miembro:
            miembro = miemb
            break
    if miembro is None:
        print("Miembro no Encontrado o Inexistente")
        return
        
    nuevo_prestamo = {
        "ID_prestamo": str(len(prestamos) + 1),
        "ID_libro":id_libro,
        "ID_miembro":id_miembro,
        "Fecha_prestamo":input("Fecha de Prestamo (YYYY-MM-DD): "),
        "Fecha_devolucion":input("Fecha de Devolucion (YYYY-MM-DD): ")
    }
    prestamos.append(nuevo_prestamo)
    libro["Disponible"] = False
    guardar_datos(libros,"libros.json")
    guardar_datos(prestamos,"prestamos.json")

#devolver libro
def devolver_libro(libros,prestamos):
    id_libro = input("Ingresar ID del libro a devolver: ")
    libro = None
    for l in libros:
        if l["ID_libro"] == id_libro:
            libro = l
            break
    if libro is None or libro["Disponible"]:
        print("El libro ya esta Disponible o no existe")
        return
    prestamo = None
    for p in prestamos:
        if p["ID_libro"] == id_libro:
            prestamo = p
            break
    if prestamo is None:
        print("Prestamo no Encontrado")
        return
    prestamos.remove(prestamo)
    libro["Disponible"] = True

    guardar_datos(libros,"libros.json")
    guardar_datos(prestamos,"prestamos.json")   

#reporte para libros prestados
def reporte_libros(libros,prestamos):
    libros_prestados = (libro for libro in libros if not libro["Disponible"])
    with open("reporte_libros.json","w") as file:
        json.dump(libros_prestados,file,indent=4)
        print("Reporte de los libros prestados generado exitosamente")

#reporte de miembros
def reporte_miembros(miembros,prestamos):
    miembros_prestamos = defaultdict(list)
    for prestamo in prestamos:
        #funcion para buscar el id de un miembro que exista en prestamo
        miembro = next((miembro for miembro in miembros if miembro["ID_miembro"] == prestamo["ID_miembro"]),None)
        if miembro:
            miembros_prestamos[miembro["Nombre"]].append(prestamo)
    with open("reporte_miembros.json","w") as File:
        json.dump(miembros_prestamos,File,indent=4) 
    print("Reporte de miembros generado exitosamente")

def gestionar():
    libros = leer_datos("libros.json")
    miembros = leer_datos("miembros.json")
    prestamos = leer_datos("prestamos.json") 

    while True:
        print("\n***Menu Biblioteca***")
        print("1- Añadir Libro")
        print("2- Buscar Libro")
        print("3- Listar Libros")
        print("4- Añadir Miembro") 
        print("5- Buscar Miembro")
        print("6- Listar Miembros")
        print("7- Prestar Libro")
        print("8- Devolver Libro")
        print("9- Listar Prestamos")
        print("10- Generar Reporte de Libros Prestados")
        print("11- Generar Reporte de Miembros con Prestamos")
        print("0- Salir del Menu")

        opc = input("Seleccione Opcion Valida: ")

        if opc == "1":
            agregar_libro(libros)
        elif opc == "2":
            buscar_libro(libros)
        elif opc == "3":
            listar_libros(libros)
        elif opc == "4":
            agregar_miembro(miembros)
        elif opc == "5":
            buscar_miembro(miembros)
        elif opc == "6":
            listar_miembros(miembros)
        elif opc == "7":
            prestar_libro(libros,miembros,prestamos)
        elif opc == "8":
            devolver_libro(libros,prestamos)
        elif opc == "9":
            listar_prestamos(prestamos)
        elif opc == "10":
            reporte_libros(libros,prestamos)
        elif opc == "11":
            reporte_miembros(miembros,prestamos)
        elif opc == "0":
            print("Cerrando Sistema...")
            print("*"*20)
            break
        else:
            print("Opcion Invalida...")

gestionar()                