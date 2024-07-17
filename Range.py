'''
a = int(input("Ingresa un numero: "))
b = int(input("Ingresa un segundo numero: "))
for o in range(a,b+1,2):
    print("Rango de: ",o)
'''
#Ejercicio2 Funciones
lista = []
par = []
impar = []  
def agregar():
    opc = 0
    while opc <= 5:
     i = int(input("Ingresa un numero para la lista: "))
    lista.append(i)
    opc += 1

def orden():
    lista.sort()

    for i in lista:
       if(i % 2 == 0):
          par.append(i)
       else:
          impar.append(i)
          
print(par)
print(impar)    

agregar()
orden()