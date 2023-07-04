def salario_neto():
    print ("Porgrama 20 \n calcule el salario neto de los empleados de su empresa \n ")
    SB1 = input("Salario bruto del empleado ")
    salariobruto = float(SB1)
    segurosocial = salariobruto * 0.08
    seguroeducativo = salariobruto * 0.02
    impuestos = salariobruto * 0.15
    prestamos = 100
    salarioneto = salariobruto - segurosocial - seguroeducativo - impuestos - prestamos
    print("El descuento de seguro social es : ", round (segurosocial,2))
    print("El descuento de seguro educativo es: ", round (seguroeducativo,2))
    print("El descuento con impuesto es: ", round (impuestos,2))
    print("El descuento del prestamo es: ", round (prestamos,2))
    print("El total del salario neto es: ", round (salarioneto,2))
salario_neto()