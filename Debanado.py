###JUEVES###
'''''
#Ejercicio1
palabra1 = input("Ingresa una palabra")
palabra2 = input("Ingresa otra palabra")
#Si las ultimas 3 letras son iguales rima
if(palabra1[-3:] == palabra2[-3:]):
    print("Las palabras riman")
#Si las ultimas 2 letras coinciden rima poco    
elif(palabra1[-2:] == palabra2[-2:]):
    print("Las palabras riman poco")
else:
    print("Las palabras no riman")

#Ejercicio2    
voto = input("Ingresa un partido politico",
             "\nA: partido rojo",
             "\nB: partido verde",
             "\nC: partido azul")
if(voto == "A"):
    print("Votaste por partido rojo")
elif(voto == "B"):
    print("Votaste por partido verde")
elif(voto == "C"):
    print("Votaste por partido azul")
else:
    print("Opcion erronea")


#Debanado de Cadenas
#Ejercicio1
lista = [20,50,"Curso","Python",3.14]
print(lista)
numero = input("Ingresa un numero")
numero2 = input("Ingresa otro numero")
lista[0] = numero
lista[1] = numero2
print(lista)
'''''
#Ejercicio2
lista2 = [1,2,3,4,5,6,7,8,9,10]
#insertar no reemplaza, mueve un espacio de memoria
lista2.insert(4,5*2)
lista2.insert(7,8*2)
lista2.insert(9,10*2)
print(lista2)