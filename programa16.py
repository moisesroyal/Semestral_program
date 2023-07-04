def evaluacion_final():
    print ("Programa 16. \nPrograma que calcule la evaluacion final \n")
    C1 = float(input(" primera evaluacion "))
    C2 = float(input(" segunda evaluacion "))
    C3 = float(input(" tercera evaluacion "))
    C4 = float(input(" cuarta evaluacion "))
    C5 = float(input(" quinta evaluacion "))

    Eva1 = 0.20
    Eva2 = 0.15
    Eva3 = 0.25
    Eva4 = 0.10
    Eva5 = 0.30

    EvaluacionFinal = float((Eva1 * C1) + (Eva2 * C2) + (Eva3 * C3) + (Eva4 * C4) + (Eva5 * C5)/100)
    print("Evaluacion final: ", EvaluacionFinal)
evaluacion_final()