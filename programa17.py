def convierta_unidades():
    print('Programa 17 convierta unidades ')
    mt = float(input('Valor de metro: '))
    gr = float(input('Valor de gramo: '))
    kl = float(input('Valor de kilogramo: '))
    cm = float(input('Valor de centimetro: '))
    c1 = kl * 1000
    print(c1)
    c2 = gr / 1000
    print(c2)
    c3 = mt * 100
    print(c3)
    c4 = cm / 100
    print(c4)
convierta_unidades()