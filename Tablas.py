#Ejercicio1
'''''
#pedir numero y mostrar la tabla de ese numero
i = int(input("Ingresa un numero: ")) 
#auxiliar para iterar
o = 1
print("Tabla del: {}".format(i))
while o <= 10:
    print(o," x ",i," = ", o * i)
    o += 1

#Ejercicio2
# pedir edad y mostrar todos los años que cumplio
edad = int(input("ingresa tu edad: "))
opc = 1
while(opc <= edad):
    print("Tienes: {} años cumplidos".format(opc))
    opc += 1
'''''
lista = [1,2,3,4,5,6,7,8,9,10]
lista[3] = 10                                                     
for i in lista:
    print("pito ",i)