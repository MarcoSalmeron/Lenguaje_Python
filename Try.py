#Ejercicio1
#funcion con dos parametros y retorne division
#exepxiones: division por 0 y enctradas no numericas


#definir funcion
def division(a,b):
  try:
  #verificar que haya un numero
    if not isinstance(a,(int,float)):
     raise TypeError("Tipo de dato invalido para: ",a)
    if not isinstance(b,(int,float)):
     raise TypeError("Tipo de dato invalido para: ",b) 
    if isinstance(a <= 0):
      raise ZeroDivisionError("Valor Nulo para ",a)
    if isinstance(b <= 0):
      raise ZeroDivisionError("Valor Nulo para ",b)
                                                                                      
  except TypeError as error:
    print(f"Error: {str(error)}")
  except ZeroDivisionError as error2:
    print(f"Error: {str(error2)}")  
  except:
    print("Opcion Invalida\n")
  return (f"Divicion entre {a} y {b} = {a/b}")

  
      
resultado = division(5,0)
print(resultado)
                                                                                                                                                                                                                                      
