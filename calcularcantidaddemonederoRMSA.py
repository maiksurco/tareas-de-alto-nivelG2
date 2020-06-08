def calcularcantidaddemonederoRMSA():
    #datos de entrada 
    billetes_10=int(input("ingrese cuantos billetes se tiene de 10 $ :"))
    billetes_20=int(input("ingrese cuantos billetes se tiene de 20 $ :"))
    billetes_50=int(input("ingrese cuantos billetes se tiene de 50 $ :"))
    monedas_10=int(input("ingrese cuantas monedas de 10 se tiene :"))
    monedas_5=int(input("ingrese cuantas monedas de 5 se tiene "))
    monedas_1=int(input("ingrese cuantas monedas de 1 se tiene :"))
    #proceso
    resultado=(billetes_10*5)+(billetes_20*5)+(billetes_50*25)
    resultado1=(monedas_10*10)+(monedas_5*5)+monedas_1
    total=resultado1+resultado
    #datos de salida
    print(f"la suma de billetes es: {resultado} $")
    print(f"la suma de monedas es: {resultado1} pesos")
    print(f"la suma total es : {total}")

calcularcantidaddemonederoRMSA()