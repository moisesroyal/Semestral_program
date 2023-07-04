def regla_de_3():
    print ("Programa 11. \n Programa que realize un calculo con la regla de 3 \n")
    N2 = input("Valor de B ")
    N3 = input("Valor de C ")
    N1 = input("Valor de A ")
    A = float(N1)
    B = float(N2)
    C = float(N3)
    X = (B * C) / A
    print("El resultado es: ", round (X,2))
regla_de_3()
