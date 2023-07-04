def numeros_pares_impares():
    numero = 0

    while numero <= 15:
        if numero % 2 == 0:
            print(numero, "es un número par")
        else:
            print(numero, "es un número impar")
        numero += 1
numeros_pares_impares()