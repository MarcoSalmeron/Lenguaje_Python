#Ejercicio1
'''''
#Diccionario con paises con valor de capitales
Diccionario = {"Guatemala": "Ciudad de Guatemala", "El Salvador" : "San Salvador", "Honduras":"Honduras", "Nicaragua":"Managua", "Costa Rica":"San Jose", "Venezuela":"Caracas", "España":"Madrid"}

pais =(input("Ingresa un pais para conocer su capital: "))
#caracter tipo logico es cierto o es falso
opc = pais.title() in Diccionario
if opc:
    print(f"Capital : {Diccionario[pais.title()]}")
else:
    print("opc no valida")
'''''
#Ejercicio2
#Diccionario con numero de jugadores
Diccionario2 = {1:"Casillas", 15:"Ramos", 3:"Pique", 5:"Puyol", 11:"Capdevila", 14:"Xabi Alonso", 16:"Busquets", 8:"Xavi Hernandez", 18:"Pedrito", 6:"Iniesta", 7:"Villa"}
print(f"{Diccionario2.keys()}")
num = int(input("Ingresa un numero de jugador: "))
print(f"Jugador: {num}. {Diccionario2[num]}")

