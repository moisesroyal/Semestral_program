def calcular_costo():
    print ("Programa 14. \n Programa que calcule el costo total de combustible \n")
    GA = input("Valor de Precio de Gasolina ")
    LT = input("Valor de Cantidad de litros ")
    Gasolina = float(GA)
    Litro = float(LT)
    CostoSinImpuesto = Gasolina * Litro
    CostoTotal = CostoSinImpuesto * 1.07
    print("El costo total es: ", round (CostoTotal,2))
calcular_costo()