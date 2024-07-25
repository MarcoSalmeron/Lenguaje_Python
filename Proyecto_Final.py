#gestionar inventario Amazon
#funciones: leer,mostrar,enlistar,eliminar,reporte

import json
from collections import defaultdict
#leer archivo
def leer(nombre_archivo):
    try:
        with open(nombre_archivo,"r") as File:
            return json.load(File)
    except FileNotFoundError:
        print("Archivo no Encontrado...")
        return []
    except json.JSONDecodeError:
        print("Error al Decodificar Archivo .JSON")
        return []

#mostrar contenido del archivo
def mostrar(nombre_archivo):
    for datos in nombre_archivo:
        print(json.dumps(datos,indent=4))   

#guardar datos
def guardar(datos,nombre_archivo):
    try:
        with open(nombre_archivo,"w") as File:
            json.dump(datos,File,indent=4)
    except Exception as ex:
        print(f"Error al guardar en {nombre_archivo} : Error {ex}")

#buscar productos
def buscar(productos):
    criterio = input("Ingresa el Nombre del Producto que Quieres Buscar: ")

    for producto in productos:
        if producto["Nombre"].lower() == criterio.lower():
            print(json.dumps(producto,indent=4))
            return producto
    print("Producto no Encontrado, intente un nombre valido")
    return None

#listar productos
def listar(productos):
    for producto in productos:
        print(producto)

#agregar productos
def vender(productos):
    nombre = input("Ingresa el nombre del producto que quieres vender: ")
    categoria = input("Ingresa la categoria del producto: ")
    precio = float(input("Ingresa el precio del producto: "))
    cantidad = int(input("Ingresa la cantidad de productos que quieres vender: "))
    estado = input("Ingresa el estado del producto: ")

    nuevo_producto = {
        "ID_producto": str(len(productos) + 1),
        "Nombre":nombre,
        "Categoria":categoria,
        "Precio":precio,
        "Cantidad":cantidad,
        "Estado":estado
    }
    productos.append(nuevo_producto)
    guardar(productos,"Amazon.json")

#eliminar productos
def comprar(productos):
    nombre_eliminar = input("Ingresa el Nombre del Producto que quieres adquirir: ")

    for i, producto in enumerate(productos):
        if producto["Nombre"].lower() == nombre_eliminar.lower():
            cantidad_vendida = int(input("Ingresa la cantidad que deseas adquirir: "))
            if cantidad_vendida > producto["Cantidad"]:
                print("Cantidad excesiva al stock de inventario")
                continue
            elif producto["Cantidad"] == 1:
                del productos[i]
                print(f"Ahora el producto: {nombre_eliminar} estara fuera de stock")
                guardar(productos,"Amazon.json")
                return productos
            producto["Cantidad"] = producto["Cantidad"] - cantidad_vendida
            guardar(productos,"Amazon.json")   
            return productos
        else:
            print("Producto no Encontrado...")
    return None    
                     
#reporte de productos
def reporte_productos(productos):
    valor_total = sum(producto["Cantidad"] * producto["Precio"] for producto in productos)

    inventario_categoria = defaultdict(lambda: {"Cantidad":0,"Ingresos_Categoria":0.0})
    productos_categoria = defaultdict(list)

    for producto in productos:
        categoria = producto["Categoria"]
        cantidad = producto["Cantidad"]
        ingresos = producto["Cantidad"] * producto["Precio"]
        nombre = producto["Nombre"]

        inventario_categoria[categoria]["Cantidad"] += cantidad
        inventario_categoria[categoria]["Ingresos_Categoria"] += ingresos
        productos_categoria[categoria].append(nombre)

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
        guardar(reporte,"reporte_amazon.json")

#gestionar menu
def gestionar():
    nombre = "Amazon.json"
    productos = leer(nombre)

    while True:
        print("\n***Amazon Menu***")
        print("1- Mostrar Productos")
        print("2- Buscar Productos")
        print("3- Vender Producto")
        print("4- Comprar Producto")
        print("5- Generar Reporte de inventario")
        print("6- Salir de Menu")
        print("*" * 17)

        opc = int(input("Ingresa una opcion valida: "))

        if opc == 1:
            mostrar(productos)
        elif opc == 2:
            buscar(productos)
        elif opc == 3:
            vender(productos)
        elif opc == 4:
            comprar(productos)
        elif opc == 5:
            reporte_productos(productos)
        elif opc == 6:
            print("Saliendo del Menu...")
            print("*" * 17)
            break
        else:
            print("Opcion no valida, intente nuevamente")                                     

gestionar()