def cantidad_compra():
    print ("Programa 15. \nPrograma que calcule la cantidad total de las compras \n")
    C1 = input("Valor de la primera compra")
    C2 = input("Valor de la segunda compra")
    C3 = input("Valor de la tercera compra")
    while C1,C2,C3 == 1:
    Compra1 = float (C1)
    Compra2 = float (C2)
    Compra3 = float (C3)
    Total = (Compra1 + Compra2 + Compra3) * 1.07
    print("El total de las compras es: ", round (Total,2))
cantidad_compra()
