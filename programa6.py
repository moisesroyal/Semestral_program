def area_trapecio():
    print('programa6')
    i1 =  input("escriba el valor de base1: ")
    i2 =  input("escriba el valor de base2: ")
    i3 =  input("escriba el valor de altura: ")

    base1 = float(i1)
    base2 = float(i2)
    altura = float(i3)
    A= round((base1 + base2) * altura)/2
    AR = round(A,2)
    print("el area de un trapecio es: ", A)
area_trapecio()