import importlib
import time

programas = [
    "programa1",
    "programa2",
    "programa3",
    "programa4",
    "programa5",
    "programa6",
    "programa7",
    "programa8",
    "programa9",
    "Programa10",
    "Programa11",
    "programa12",
    "programa13",
    "programa14",
    "programa15",
    "programa16",
    "programa17",
    "programa18",
    "programa19",
    "programa20",
    "programa21",
    "programa22",
    "programa23",
    "programa24",
    "programa25",
    "programa26",
    "programa27",
    "programa28",
    "programa29",
    "programa30",
    "programa31",
    "programa32",
    "programa33",
    "programa34",
    "programa35",
    "programa36",
    "programa37"
    
]

def Abrir_lista():
    print("Listado de programas")
    for i, programa in enumerate(programas, start=1):
        print(f"{i}. {programa}")
    print("0. Salir")

def ejecutar_programa(num_programa):
    if num_programa >= 1 and num_programa <= len(programas):
        programa = programas[num_programa - 1]
        try:
            programa_lista = importlib.import_module(programa)
            programa_lista.ejecutar()
        except (ImportError, AttributeError):
            print("espere 5s.")
    else:
        print("Opción inválida.")

    time.sleep(5) 

while True:
    Abrir_lista()
    opcion = input("Elige un número de programa: ")
    if opcion == '0':
        print("Fin")
        break
    try:
        num_programa = int(opcion)
        ejecutar_programa(num_programa)
    except ValueError:
        print("Elige un número de programa válido.")

