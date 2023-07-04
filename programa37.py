def suma_numeros_pares():
    suma = 0
    n1 = 1
    while n1 != 20:
        n1 = int(input("Valor: "))
        if n1 != 0:
            if n1 % 2 == 0:
                suma = suma + n1
    print ("La suma total de numeros pares: ",suma)
suma_numeros_pares()