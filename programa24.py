def numero_mayor():
    #programa que muestre que numero es el mayor

    valor1 = int(input("escriba el 1numero: "))
    valor2 = int(input("escriba el 2numero: "))
    valor3 = int(input("escriba el 3numero: "))
    if valor1 > valor2 and valor1 > valor3:
        print("El numero mayor es valor1 = ", valor1)
    if valor2 > valor1 and valor2 > valor3:
        print("El numero mayor es valor2 = ", valor2)
    if valor3 > valor1 and valor3 > valor2:
        print("El numero mayor es valor3 = ", valor3)
    print ('final del programa ')
numero_mayor()
