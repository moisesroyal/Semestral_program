
def convierta_una_cantidad():
    print ("Programa 10. \nPrograma que convierta una cantidad \n")
    ME = input("Valor de Metro ")
    Metro = float(ME)
    A = Metro *  3.281
    B = Metro * 39.37
    print("El resultado de metro a pie es: ", round (A,2))
    print("El resultado de metro a pulgada es: ", round (B,2)) 
convierta_una_cantidad()
