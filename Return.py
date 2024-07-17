#Ejercicio1
'''
a = int(input("Ingresa un numero\n"))
b = int(input("Ingresa otro numro\n"))

#definir funcion
def comparar(a,b):
    if(a > b):
        return 1
    elif(a < b):
        return -1
    elif(a == b):
        return 0
print(comparar(a,b))

'''
#Ejercicio2
while True:
 iva = 21
 can = input("Ingresa una cantidad a Facturar\n")
 #validar si contiene algo 
 if can.strip():
    try:
     print("Quieres Ingresar Iva?  1/SI : 2/NO")
     opc = int(input())
     break
    except:
     print("Valor no encontrado")

if(opc == 1):
   iva = int(input("Ingresa Iva\n"))
   print("El Iva sera del ",iva,"%")
elif(opc == 2):
   print("El Iva aplicado sera del ",iva,"%")
else:
   print("Opcion no valida...")
   


#definir funion
def factura(can,iva):
    IVA = iva / 100
    factura = can * IVA
    total = can + factura
    return total

print("\n"f"Total con Iva: {factura(can,iva)} $$$ pesos mexicanos $$$")