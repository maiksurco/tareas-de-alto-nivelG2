def calcularventasdevendedorRMSA():
    total=0
    contador=1
    #datos de entrada y proceso
    while contador<=8:
        costo=int(input(f"ingrese costo de objeto vendido {contador} :"))
        total=total+costo
        contador=contador+1
    #datos de salida
    print(f"el total de ventas es: {contador}")
    print(f"el total de costo de ventas es: {total}")

calcularventasdevendedorRMSA()