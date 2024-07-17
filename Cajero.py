#funcion que reciva transacciones en forma de diccionarios
#retorno: balance final de la cuenta, cantidad de transacciones (deposito/retiro) y diccionario con fechas como claves con los montos de las transacciones como valor
#claves: id,monto,tipo,fecha(formato: año,mes,dia)
from datetime import datetime

def Recibo(transacciones):
    #balance final
    Monto_Disponible = 0
    #cantidad por tipo
    cantidad_categoria = {"Deposito": 0, "Retiro":0}
    #transaccion por fecha
    transacciones_retorno = {}

    #recorrer argumento para verificar campos
    for i in transacciones:
        try:
            #validar claves del diccionario
            if not all(key in i for key in ["id","monto","tipo","fecha"]):
                raise KeyError("Falta llenar campos o claves Invalidas!!!")
            #datos a extraer
            ID = i["id"]
            Monto = i["monto"]
            Tipo = i["tipo"]
            fecha = i["fecha"]
            #Fecha = datetime.strptime(fecha,format("%Y-%m-%d"))

            #Validar campos Extraidos
            if not isinstance(Monto,(int,float) or Monto <= 0):
                raise ValueError("Monto Invalido (Negativo o Nulo) para Transaccion ", ID)
            if Tipo not in ["Deposito","Retiro"]:
                raise ValueError("Tipo de Transaccion Invalida!!! para ", ID)
            #verificar formato de fecha
            if not isinstance(fecha,str) or len(fecha) != 10 or fecha[4] != "-" or fecha[7] != "-":
                raise ValueError("Fecha sin el formato Año,Mes,Dia para transaccion ", ID)
            if not isinstance(ID,str):
                raise TypeError("ID no es cadena de texto")  
            
            #Actualizar cantidad por tipo
            if Tipo == "Retiro":
                Monto_Disponible -= Monto
                cantidad_categoria["Retiro"] += 1
            elif Tipo == "Deposito":
                Monto_Disponible += Monto
            cantidad_categoria["Deposito"] += 1 
           

            #actualizar montos por fecha
            if fecha not in transacciones_retorno:
                transacciones_retorno[fecha] = 0
            transacciones_retorno[fecha] += Monto    
        #Manejar exepciones
        except KeyError as a:
            print(f"Error: {str(a)}")
        except TypeError as e:
            print(f"Error: {str(e)}")
        except ValueError as o:
            print(f"Error: {str(o)}")
    return {
        "Balance Final: ": Monto_Disponible,
        "Cantidad por Tipo: ": cantidad_categoria,
        "Monto por Fecha: ": transacciones_retorno
    }        

Pagos = [
    {"id":"PAGO01", "retiro":3500,"tipo":"Deposito", "fecha":"2004-01-23"}, #Fallo en monto
    {"id":"PAGO02", "monto":1000,"tipo":"Retiro", "fecha":"23-01-2004"}, #fallo en fecha
    {"id":"PAGO03", "monto":2000,"tipo":"Videojuegos", "fecha":"2006-03-23"} #fallo en tipos
]

resultado = Recibo(Pagos)
print(resultado)