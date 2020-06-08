def calcularcostodearticulosRMSA():
    #datos de entrada
    precio1=int(input("ingrese el precio de articulo 1:"))
    precio2=int(input("ingrese el precio de articulo 2:"))
    precio3=int(input("ingrese el precio de articulo 3:"))
    articulo1=int(input("ingrese el costo de articulo 1:"))
    articulo2=int(input("ingrese el costo de articulo 2:"))
    articulo3=int(input("ingrese el costo de articulo 3:"))
    #proceso 1:
    if precio1>=200:
        costo1=articulo1*0.15
    elif precio1>100 and precio1<200:
                costo1=articulo1*0.12
    else:
                    costo1=articulo1*0.10
    #proceso 2:
    if precio2>=200:
        costo2=articulo2*0.15
    elif precio2>100 and precio2<200:
                costo2=articulo2*0.12
    else:
                    costo2=articulo2*0.10
    #proceso 3:
    if precio3>=200:
        costo3=articulo3*0.15
    elif precio3>100 and precio3<200:
                costo3=articulo3*0.12
    else:
                    costo3=articulo3*0.10
    #datos de salida:
    print(f"el precio de articulo 1 segun el precio es: {articulo1}")
    print(f"el descuento que se da de acuerdo al costo de articulo es: {costo1}")
    print(f"el precio de articulo 2 segun el precio es: {articulo2}")
    print(f"el descuento que se da de acuerdo al costo de articulo es: {costo2}")
    print(f"el precio de articulo 3 segun el precio es: {articulo3}")
    print(f"el descuento que se da de acuerdo al costo de articulo es: {costo3}")
    
calcularcostodearticulosRMSA()