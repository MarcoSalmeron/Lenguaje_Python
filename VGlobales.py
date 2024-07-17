##Ejemplo##
#guardar tuplas
'''
def argumento(*num):
    for i in num:
        print(i)

argumento((1,2,3,4,5)) 
print(type(argumento()))       

#Ejercicio1
#dos funciones (area cuadrado, area circulo)

def areaCuadrado(base,altura):
    area = (base)(altura)
    return "\nArea del Cuadrado: ",area

def areaCirculo(radio):
    area = (radio**2)(3.14)
    return "\nArea del Circulo: ",area

#ingresar datos independientes en el metodo
print(areaCuadrado(5,10))
print(areaCuadrado(100,200))
print(areaCirculo(500))
print(areaCirculo(50))
'''
#Ejercicio2
#funcion para lista y devolver longitud
def lista(*objeto):
    #print(type(objeto))
    for i in objeto:
        print("Lista: ",i)
    return len(*objeto)   

print(lista((2,4,6,8,10,12,14,16,20)))