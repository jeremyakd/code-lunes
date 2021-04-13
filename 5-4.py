# pedimos un nombre por consola y lo imprimimos en la consola

# nombre = input("Hola, ingrese su nombre por favor: ===> ") # funcion de entrada

# print("hola ", nombre) # funcion de salida

# pido 2 numeros y los sumo
import re


def presentacion():
    print("Programa que permite cargar dos valores por teclado.")
    print("Efectua la suma de los valores")
    print("Muestra el resultado de la suma")
    print("*******************************")


def cargaYSuma():

    while True:
        try:
            num1 = int(input("ingrese un numero por favor."))
            num2 = int(input("ingrese un numero por favor."))

            patron = "[0-9]+"

            if re.search(patron, str(num1)):
                if re.search(patron, str(num2)):
                    print("La suma de los numeros es: ", num1+num2)
                    break

        except ValueError:
            print("Alguno de los dos valores introducidos no son correctos")
            print("Intentalo de nuevo.")

# programa principal

presentacion()
cargaYSuma()
