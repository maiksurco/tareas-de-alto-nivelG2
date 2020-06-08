def calcularahorrosanualesRMSA():
    #datos de entrada:
    contador_demes=1
    valorde_cadames=20
    resultado=0
    total=0
    #proceso:
    while contador_demes<=12:       
        valorde_cadames=int(input(f"ingrese la cantidad de dinero por cada mes {contador_demes}:"))
        resultado=resultado+valorde_cadames
        contador_demes=contador_demes+1
        total=resultado*0.1

    #datos de salida:
    print(f"el total de la inversion final de los 12 meses es: {resultado}")
    print(f"el resultado de 10 porciento anual es: {total}")

calcularahorrosanualesRMSA()