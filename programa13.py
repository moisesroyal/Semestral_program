def calcular_salario():
    print ("Programa 13. \n Programa que calcule el salario neto \n")
    SA = input("Valor de Salario bruto ")
    SAB = float(SA)
    SeguroSocial = SAB * 0.0514
    SeguroEducativo = SAB * 0.02
    CuotaPrestamo = 50
    SalarioNeto = SAB - SeguroSocial - SeguroEducativo - CuotaPrestamo
    print("El descuento de seguro social es: ", round (SeguroSocial,2))
    print("El descuento de seguro educativo es: ", round (SeguroEducativo,2))
    print("La cuota de prestamo es de: ",  (CuotaPrestamo))
    print("El salario neto es: ", round (SalarioNeto,2))
calcular_salario()