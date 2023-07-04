def calcula_el_perimetro():
    i1 =  float(input("escriba el valor de AB: "))
    i2 =  float(input("escriba el valor de BC: "))
    i3 =  float(input("escriba el valor de CD: "))
    i4 =  float(input("escriba el valor de DA: "))

    P = i1 + i2 + i3 + i4
    PR = round(P,2)
    print ("El area de un restangulo es: ", PR)
calcula_el_perimetro()