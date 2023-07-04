def temperatura():
    # Programa 22 - Calculo de temperatura

    temperatura = float(input("Escriba la temperatura: "))

    if temperatura < 20:
        if temperatura < 10:
            print("Nivel Azul")
        else:
            print("Nivel verde")
    else:
        if temperatura < 30:
            print("Nivel naranja")
        else:
            print("Nivel Rojo")
        
temperatura()