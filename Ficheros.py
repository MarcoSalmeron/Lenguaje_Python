'''
def recibo(nombre_archivo):
    precio_total = 0.0

    try:
        with open(nombre_archivo,"r") as Archivo:
            for linea in Archivo:
                try:
                    #validar formato del contenido en el archivo
                    producto,precio = linea.strip().split(":") #metodo para eliminar espacios y metodo para separar ":"
                    precio_total += float(precio)
                except ValueError:
                    print("Formato Incorrecto en la Linea: ",linea.strip())    
        return precio_total
    except FileNotFoundError:
        print("Archivo no Encontrado, Necesitas Crearlo")
    except IOError:
        print("Ocurrio un Error de Entrada/Salida")                

nombre = "productos.txt"
precio_total = recibo(nombre)
print("Precio total de productos en el archivo es: $",precio_total)

'''
#Ejercicio2
def reporte(nombre_archivo,archivo_reporte):
    ingreso_total = 0
    ventas_producto = {}
    try:
        with open(nombre_archivo,"r") as Archivo:
            for lineas in Archivo:
                #verificar primer archivo
                try:
                    #limpiar espacios en blanco
                    lineas = lineas.strip()
                    if not lineas:
                        continue
                    #crea formato separando con el metodo split()
                    fecha,producto,cantidad,precio = lineas.split(",")
                    cantidad = int(cantidad.strip())
                    precio = float(precio.strip())
                    #calcular ingreso
                    ingreso = cantidad * precio
                    ingreso_total += ingreso
                    #actualizar ventas por producto
                    if producto not in ventas_producto:
                       #si esta vacio iniciamos en 0
                       ventas_producto[producto] = {"Cantidad" : 0, "Ingresos":0.0}

                    ventas_producto[producto]["Cantidad"] += cantidad
                    ventas_producto[producto]["Ingresos"] += ingreso      

                except ValueError:
                    print("Formato invalido en Linea: ",lineas.strip())
                except Exception:
                    print("Error Desconocido en Linea: ",lineas.strip())      
        #generar un reporte
        with open(nombre_reporte, "w") as reporte:
                  reporte.write(f"Ingreso Total: {ingreso_total}")
                  reporte.write("\nVentas por Producto: \n")
                  for i in ventas_producto:
                     reporte.write(f"{ventas_producto}")
    except FileNotFoundError as fe:
        print("Error: ",fe)
    except IOError as io:
        print("Error de Entrada/Salida: ",io)
    return "Ingreso Total: ",ingreso_total,"\nVentas por Producto: ",ventas_producto        

nombre_ventas = "ventas.txt"
nombre_reporte = "reporte.txt"
resultado = reporte(nombre_ventas,nombre_reporte)