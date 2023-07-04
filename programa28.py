def calificacion():
    print(' Programa28 de calificacion: ')

    for cal in range(0,5): 
        cal = float(input(' Puntos obtenidos:'))

        if (cal >= 90 and 100):
                print('Es una A')
        if (cal >= 80 and 89):
            if (cal < 90):
                print('Es una B')
        if (cal >= 70 and 79):
            if (cal < 80):
                print('Es una C')
        if (cal >= 60 and 69):
            if (cal < 70):
                print('Es una D')
        if (cal < 60):   
                print('Es una F')
                
    print('Fin del programa')
calificacion()