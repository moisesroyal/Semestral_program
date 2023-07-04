def calcula_interes():
    print ("Programa 12. \n Programa que calcule el interes a pagar por prestamo \n")
    A1 = input("Valor de Monto n")
    A2 = input("Valor de tasa ")
    A3 = input("Valor de Plazo ")
    MO = float(A1)
    TA = float(A2)
    PL = float(A3)
    TasaPorcentaje = TA * 100 
    TasaMensual = TA / 12
    Cuota =  MO * (TasaMensual /(1 -(1 + TasaMensual )**(- PL)))
    InteresMensual = MO * TasaMensual
    CapitalMensual = Cuota - InteresMensual
    print("El total de cuota es: ", round (Cuota,2))
    print("El total de Interes es: ", round (InteresMensual,2))
    print("El total de capital es: ", round (CapitalMensual,2))
calcula_interes()