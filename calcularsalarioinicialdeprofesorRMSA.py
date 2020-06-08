def calcularsalarioinicialdeprofesorRMSA():
    contadoranual=1
    salario_inicial=1500
    #datos de entrada y proceso
    while contadoranual<=6:
        valordel10anual=int(input(f"ingrese los porcientos de 10 porciento anual {contadoranual} :"))
        salario_inicial=salario_inicial+valordel10anual
        contadoranual=contadoranual+1
    #datos de salida
    print(f"la suma de los porcentajes de 72 meses  {salario_inicial} :")
    print("salario del primeros 12 meses es 150 $ ")
    print("salario de 24 meses es 165 $ ")
    print("salario de 36 meses es 181 $ ")
    print("salario de 48 meses es 199 $ ")
    print("salario de 60 meses es 219 $ ")
    print("salario de 72 meses es 241 $ ")

calcularsalarioinicialdeprofesorRMSA()