def calcular_descuento():
    print('Calculadora de descuentos:')
    precio = float(input("Precio: "))
    descuento = float(input("Descuento (%): "))

    monto_descuento = precio * (descuento / 100)
    precio_final = precio - monto_descuento

    print('Total a pagar:', precio_final)

    if precio_final < 50:
        print("Oferta especial")
    else:
        print("No incluye oferta especial")

    print("\nFin del programa")

calcular_descuento()
