def calcularclavesdevehiculosRMSA():
    #datos de entrada
    tiposdevehiculos=int(input("ingrese que tipo de claves de vehiculo desea :"))
    costo=int(input("ingrese el cotso de vehiculos :"))
    #proceso
    if tiposdevehiculos==1:
        vehiculo=(costo*0.10)
    elif tiposdevehiculos==2:
            vehiculo=(costo*0.7)
    elif tiposdevehiculos==3:
                vehiculo=(costo*0.5)
    else:
                    print("no es clave de vehiculo")
    #datos de salida:
    print(f"el impuestoa pagar es: {vehiculo}")
    print(f"el costo de vehiculo es. {costo}")

calcularclavesdevehiculosRMSA()