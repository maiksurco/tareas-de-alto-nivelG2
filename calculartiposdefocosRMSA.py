def calculartipodeloteRMSA():
    #datos de entrada:
    tipodelote=int(input("ingrese color de foco"))
    lo=int(input("ingrese la cantidad de focos n"))
    #proceso:
    if tipodelote==1:
        resultado = lo*0.5
    elif tipodelote==2:
            resultado = lo*0.3
    elif tipodelote==3:
                resultado = lo*0.2
    else:
                    print("no es foco")
    #datos de salida:
    print(f"la cantidad de focos es:{lo}")
    print(f"entonces la cantidad de color: {tipodelote}")
    print(f"entonces se tiene: {resultado}")
    print("focos")

calculartipodeloteRMSA()