#funcion que reciba diccionarios retornar costo total de productos, cantidad total de productos en cada categoria
#cada diccionario representa un producto con clave nombre,precio,cantidad y categoria
def productos_lista(producto):
    cantidad_por_categoria = {}
    costo_producto = {}
    presio_total = 0

    for i in producto:
        try:
           #validar claves del diccionario
           if not all (clave in i for clave in ["nombre","precio","cantidad","categoria"]):
               raise KeyError("Faltan Elementos en el Diccionario del Producto")
           #datos a extraer
           nombre = i["nombre"]
           precio = i["precio"]
           cantidad = i["cantidad"]
           categoria = i["categoria"]
           #validar campos
           if not isinstance(precio,(int,float) or precio <= 0):
               raise ValueError("Datos no Numericos para el ",nombre)
           if not isinstance(cantidad,(int,float) or cantidad <= 0):
               raise ValueError("Cantidad no valida para el ",nombre)
           if not isinstance(categoria,str):
               raise TypeError("Categoria Invalida para el ",nombre)
           #calcular valor de productos y categoria
           precio_producto = precio * cantidad
           presio_total += precio_producto

           #agregar costo por producto en diccionario
           costo_producto[nombre] = precio_producto

           #actualizar cantidad por categoria
           if categoria not in cantidad_por_categoria:
               cantidad_por_categoria[categoria] = 0
           cantidad_por_categoria[categoria] += cantidad   

        except KeyError as a:
            print(f"Error: {str(a)}")
        except TypeError as e:
            print(f"Error: {str(e)}")
        except ValueError as o:
            print(f"Error: {str(o)}")
    
    return {
        "Costo Total" : presio_total,
        "Cantidad de Categoria" : cantidad_por_categoria,
        "Costo por Producto" : costo_producto
    }
productos = [
    {"nombre":"manzanas", "precio":5.25, "cantidad":3, "categoria":"frutas"},
    {"nombre":"aguacate", "precio":-3.0, "cantidad":3, "categoria":"frutas"},
    {"nombre":"maiz", "precio":10.0, "cantidad":0, "categoria":"frutas"},
    {"nombre":15, "precio":50.55, "cantidad":6, "categoria":15},
]
resultado = productos_lista(productos)
print(resultado)