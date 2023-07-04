def calcula_compras():
    print("\n Programa 19 que calcule la compra de 5 articulos \n")
    cmp1 = input("Precio del producto ")
    cmp2 = input("Precio del producto ")
    cmp3 = input("Precio del producto ")
    cmp4 = input("Precio del producto ")
    cmp5 = input("Precio del producto ")
    compra1 = float (cmp1)
    compra2 = float (cmp2)
    compra3 = float (cmp3)
    compra4 = float (cmp4)
    compra5 = float (cmp5)
    totalsinimpuesto = compra1 + compra2 + compra3 + compra4 + compra5
    totalconimpuesto = totalsinimpuesto * 1.07
    promediototal = totalsinimpuesto / 5
    print("El totalsinimpuesto: ", round (totalsinimpuesto,2))
    print("El totalconimpuesto: ", round (totalconimpuesto,2))
    print("El promedio total: ", round (promediototal,2))
calcula_compras()