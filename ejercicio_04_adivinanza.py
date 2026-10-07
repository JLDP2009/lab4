"""
EJERCICIO 04: Adivina el número

1. Selecciona un número entero y almacenalo en una variable. 
2. Pide al usuario que lo adivine dentro de un bucle while. 
3. En cada intento, el programa debe indicar si el número buscado es mayor o menor que el ingresado, hasta que lo adivine.
"""

var1= 53

while True:
    try:
    
        intento= int(input("Adivina el número: "))
        if intento == var1:
            print("felicitaciones,has acertado")
            break 
        elif intento < var1:
            print("Incorrecto, el numero es mayor")
        else:
            print("Incorrecto, el numero es menor")

    except ValueError:
        print("entrada no valida")