def resuelve_ecuasiones():
    print ("Programa 9. \nPrograma que resuelva ecuasiones parte2 \n")
    a1 = input("Valor de A ")
    b1 = input("Varlor de B ")
    c1 = input("Valor de C ")
    a = float(a1)
    b = float(b1)
    c = float(c1)
    c1 = float(4 * a) + (3 * b)
    c2 = float(1 * a) - 18 + ( 8 * b) - 5
    c3 = float(4 * a) + (3 * b) + 7
    c4 = float(2* a) + (3 * b) - (c**5)
    c5 = float(2 * a) + (3*b) - (c**2)
    print("El resultado de c1 es: ", round (c1,2))
    print("El resultado de c2 es: ", round (c2,2))
    print("El resultado de c3 es: ", round (c3,2))
    print("El resultado de c4 es: ", round (c4,2))
    print("El resultado de c5 es: ", round (c5,2))
resuelve_ecuasiones()