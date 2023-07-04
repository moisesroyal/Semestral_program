def area_prisma(): 
    i1 =  input("escriba el valor de largo: ")
    i2 =  input("escriba el valor de ancho: ")
    i3 =  input("escriba el valor de altura: ")

    largo = float(i1)
    ancho = float(i2)
    altura = float(i3)
    vol= largo * ancho * altura
    volR = round(vol,4)
    print("el area de un prisma rectangular es: ", volR)
area_prisma()