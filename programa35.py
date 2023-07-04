def numeros_mayor_menor():
    for A1 in range(0,10):
        A1 = int(input('ingresar numero: '))
        if A1 < 5:
            print ('Es menor que 5')
        elif A1 > 5:
            print('es mayor a 5 ')
        
        else:
            print('Es igual a 5')
            
    print('Fin del programa')
numeros_mayor_menor()