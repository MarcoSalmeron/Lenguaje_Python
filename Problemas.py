'''''
cadena = "Te quiero solo como amigo"
print(cadena[0:2])
print(cadena[-3:])
print(cadena[::-1])
print(cadena)

cadena2 = "SEPARADO"
espacio = ","
print(cadena2[0],espacio,cadena2[1],espacio,cadena2[2],espacio,cadena2[3],espacio,cadena2[4],espacio,cadena2[5],espacio,cadena2[6],espacio,cadena2[7])

###MIERCOLES###

nombre = input("Ingresa tu nombre ") 
print("Hola ",nombre)

#Ejercicio 1 Formula General
print("Ejercicio1: Formula")
a = int(input("Ingresa el valor de a: "))
b = int(input("Ingresa el valor de b: "))
c = int(input("Ingresa el valor de c: "))
x = (b ** 2)-(4*a*c)
x1 = -b+x**(1/2)/2*a
x2 = -b-x**(1/2)/2*a
print("Solucion de Ecuacion: ", x1 , " y ", x2)

#Ejercicio2 Calificacion Final

print("Ejercicio2: CalificacionFinal")
P1 = int(input("Ingresa el valor del Parcial 1: "))
P2 = int(input("Ingresa el valor del Parcial 2: "))
P3 = int(input("Ingresa el valor del Parcial 3: "))
PP = (P1 + P2 + P3)/3
EP = int(input("Ingrese el valor del Examen Parcial"))
EF = int(input("Ingresa el valor del Examen Final"))
PROM = (PP + 2*EP + 3*EF)/6
print("La calificacion es: ",PROM)

'''''
may = input("ingrese una mayuscula")
min = input("ingrese una minuscula")
print(may.lower(), " y ", min.upper())

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
genero = input("Ingresa tu genero: ")
print("Tu nombre: ",nombre,
      "\nTu Edad: ",edad,
      "\nEres: ",genero)
