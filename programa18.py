def interes_compuesto():
    print('Programa 18')
    print('programa que calcule el interes compuesto ')
    Cinicial = float(input('Cantidad inicial: '))
    tasa = float(input('Cantidad tasa: '))
    periodo = float(input('Cantidad periodo: '))
    capital_final = Cinicial * (1 + tasa)**periodo
    print('El total es: ',capital_final)
    
interes_compuesto()