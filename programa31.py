def par_impar():
    valor1 = 0

    while valor1 <= 15:
        if valor1 % 2 == 0:
            print(valor1, "es par")
        else:
            print(valor1, "es impar")
        valor1 += 1
par_impar()