def calculartablademultiplicarRMSA():
    #datos de entrada
    num=int(input("ingrese con que numero de la tabla de ocho desea multiplicar :"))
    #proceso
    if num>=0 and num <=12:
        resultado=8*num
    else:
            print("no es multiplicacion")
    #dtos de salida
    print(f"la respuesta es: {resultado}")

calculartablademultiplicarRMSA()