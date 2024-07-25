#Ejercicio
#gestionar el inventario de una tienda a travez de un archivo json
#formato de inventario = id,nombre,categoria,cantidad,precio
#funciones = leer y mostrar inventario, agregar un producto, buscar producto por ID, 
#actualizar cantidad de un producto,eliminar un producto del inventario, generar reporte del inventario
import json
from collections import defaultdict
#funcion leer archivo
def leer(nombre_archivo):
    try:
        with open(nombre_archivo,"r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Archivo no Encontrado, creando nuevo archivo...")
        return []    
    except json.JSONDecodeError:
        print("Error al decodificar archivo .JSON ")
        return []    
    
def guardar(nombre_archivo,productos):
    try:
        with open(nombre_archivo,"w") as file:
            json.dump(productos,file,indent=4)
    except IOError:
        print("Error al escribir en el Archivo!! ") 

def mostrar(productos):
    for producto in productos:
        print("*" * 20)
        print(f"ID: {producto["ID"]}")
        print(f"Nombre: {producto["Nombre"]}")
        print(f"Categoria: {producto["Categoria"]}")
        print(f"Cantidad: {producto["Cantidad"]}")
        print(f"Precio Unitario: {producto["Precio"]}")   
        print("*" * 20)

def agregar(productos):
    id_producto = input("Ingresa un ID para el producto: ")
    nombre = input("Ingresa el nombre del producto: ")
    categoria = input("Ingresa la categoria: ")
    cantidad = int(input("Ingresa la cantidad del producto: "))
    precio = float(input("Ingresa el precio del producto: "))
    nuevo_producto = {
        "ID":id_producto,
        "Nombre":nombre,
        "Categoria":categoria,
        "Cantidad":cantidad,
        "Precio":precio,
    }
    productos.append(nuevo_producto)
    return productos

def buscar(nombre_buscar,productos):
    for producto in productos:
        if producto["ID"] == nombre_buscar or producto["Nombre"].lower() == nombre_buscar.lower():
            return producto
    return None

def actualizar_cantidad(productos):
    id_producto = input("Ingresa el ID del producto: ")
    nueva_cantidad = int(input("Ingresa la nueva cantidad: "))
    for producto in productos:
        if producto["ID"] == id_producto:
            producto["Cantidad"] = nueva_cantidad
            return productos
    return None

def eliminar(productos):
    id_producto = input("Ingresa el ID del producto a eliminar: ")
    for i, producto in enumerate(productos):
        if producto["ID"] == id_producto:
            del productos[i]
            return productos
    return None

def reporte_archivo(productos):
    #calcular valor total
    valor_total = sum(producto["Cantidad"] * producto["Precio"] for producto in productos)

    #productos por categoria
    inventario_categoria = defaultdict(lambda: {"Cantidad":0,"Ingresos_Categoria":0.0})
    productos_categoria = defaultdict(list)
    
    #procesar productos en inventario
    for producto in productos:
        categoria = producto["Categoria"]
        cantidad = producto["Cantidad"]
        ingresos = producto["Cantidad"] * producto["Precio"]
        nombre = producto["Nombre"]

        inventario_categoria[categoria]["Cantidad"] += cantidad
        inventario_categoria[categoria]["Ingresos_Categoria"] += ingresos
        productos_categoria[categoria].append(nombre)

        #construir reporte
        reporte = {
            "Valor de Inventario":valor_total,
            "Inventario por Categoria":{
                categoria : {
                "Cantidad":datos["Cantidad"],
                "Ingresos_Categoria":datos["Ingresos_Categoria"]
            }
            for categoria,datos in inventario_categoria.items()
          },
            "Productos por Categoria" :{
                categoria : inventario
                for categoria,inventario in productos_categoria.items()
            }
        }
    #guardar cambios
    with open("reporte.json","w") as archivo:
        json.dump(reporte,archivo,indent=4)
        print("Reporte Generado con Exito!")    

def gestionar():
    reporte = "reporte.json"
    nombre = "inventario.json"
    productos = leer(nombre)

    while True:
        print("***Menu***")
        print("1- Mostrar Inventario")
        print("2- Agregar Producto")
        print("3- Buscar Producto por Nombre o ID")
        print("4- Actualizar Cantidad de un Producto")
        print("5- Eliminar Producto")
        print("6- Generar Reporte del Inventario")
        print("7- Salir")
        opc = int(input("Ingresa una Opcion Valida: "))
        if opc == 1:
            mostrar(productos)
        elif opc == 2:
            productos = agregar(productos)
            guardar(nombre,productos)
        elif opc == 3:
            busqueda = input("Ingresa el Nombre o Id del producto a buscar: ")
            producto = buscar(busqueda,productos)
            if producto:
                print("*" * 20)
                print(f"ID: {producto["ID"]}")
                print(f"Nombre: {producto["Nombre"]}")
                print(f"Categoria: {producto["Categoria"]}")
                print(f"Cantidad: {producto["Cantidad"]}")
                print(f"Precio Unitario: {producto["Precio"]}")   
                print("*" * 20)
            else:
                print("Producto no Encontrado")
        elif opc == 4:
            inventario_actualizado = actualizar_cantidad(productos)
            if inventario_actualizado is not None:
               productos = inventario_actualizado
               guardar(nombre,productos)
            else:
                print("Productos no encontrado...")
        elif opc == 5:
            inventario_actualizado = eliminar(productos)
            if inventario_actualizado is not None:
               productos = inventario_actualizado
               guardar(nombre,productos)
            else:
                print("Producto no Encontrado")
        elif opc == 6:
            reporte_archivo(productos)
        elif opc == 7:
            print("Saliendo del Menu...")
            print("***"*20)
            break
        else:
            print("Opcion no Valida")               
                              
gestionar()






