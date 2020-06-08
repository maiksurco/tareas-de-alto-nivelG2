def calculareltotaldecajaregistradoraRMSA():
    contador=1
    resultado=0
    #datos de entrada y proceso
    while contador<=15:
        dinero=int(input(f"ingrese el costo de cada bollite o moneda {contador}:"))
        resultado=resultado+dinero
        contador=contador+1
    #datos de salida:
    print(f"el monto total de dinero que se encontraba en caja es: {resultado} $")

calculareltotaldecajaregistradoraRMSA()