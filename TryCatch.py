def lista(estudiantes_lista):
        #datos a almacenar 
        edad_total = 0
        calif = {}
        estudiantes = 0
        
        for i in estudiantes_lista:
            try:    
            #validar los campos del diccionario     
                if not all (key in i for key in ["nombre", "edad", "calificacion"]):
                 raise KeyError("Faltan Elementos")
            #datos a extraer 
                nombre = i["nombre"]
                edad = i["edad"]
                calificaciones =i["calificacion"]
            #validar edad y calificacion
                if not isinstance(edad,(int,float) or edad <= 0):
                 raise ValueError("Edad no valida para ",(nombre))
                if not isinstance(calificaciones,list) or not all (isinstance(calificacion, (int, float)) for calificacion in calificaciones):
                 raise TypeError("Calificaciones Invalidas para",(nombre))
             
             #calcular edad y promedio del estudiante
                edad_total += edad
                estudiantes += 1
             #asignar a cada alumno un promedio
                calif[nombre] = sum(calificaciones) / len(calificaciones)
                edad_prom = edad_total / estudiantes
             #manejar esepciones
            except KeyError as a:
                print(f"Error {str(a)}")
            except ValueError as e:
                print(f"Error {str(e)}")
            except TypeError as o:
                print(f"Error {str(o)}")
        if estudiantes == 0:
            return "Ningun Estudiante Valido"   
            
        return {"Edad_Promedio: " : edad_prom, "Calificacion_Promedio: " : calif}


#llamar funcion con lista dentro de diccionario dentro de lista
estudiantes = [
    {"nombre":"juan", "edad" : 20, "calificacion": [60,80,70]},"\n",
    {"nombre":"marco", "edad" : 22, "calificacion": [50,60,70]}
]
print(lista(estudiantes))