
def determinar_tipo_triangulo():
    A1 = float(input('Primera Longitud: '))
    B2 = float(input('Segunda Longitud: '))
    C3 = float(input('Tercera Longitud: '))

    if A1 == B2 and B2 == C3:
        print('Es equilátero')
    elif A1 == B2 or B2 == C3 or C3 == A1:
        print('Es isósceles')
    else:
        print('Es escaleno')

determinar_tipo_triangulo()
