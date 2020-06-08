def calcularcalificacionesdealumnosRMSA():
    #datos de entrada
    tiposdealumno=int(input("ingrese el tipo de alumno para saber su calificacion :"))
    #proceso
    if tiposdealumno==1:
        alumno=(15+14+17+19)/4
    elif tiposdealumno==2:
            alumno=(20+15+2+18)/4
    elif tiposdealumno==3:
                alumno=(8+9+11+12)/4
    elif tiposdealumno==4:
                    alumno=(13+9+5+20)/4
    else:
                        print("no hay calificacion")
    #datos de salida:
    print(f"el promedio de alumno es : {alumno}")
    print("2 alumnos aprobaron con : 16.25 y 13.75")
    print("2 alumnos desaprobaron con : 10 y 11.75")

calcularcalificacionesdealumnosRMSA()