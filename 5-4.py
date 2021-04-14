# pedimos un nombre por consola y lo imprimimos en la consola

# nombre = input("Hola, ingrese su nombre por favor: ===> ") # funcion de entrada

# print("hola ", nombre) # funcion de salida

# pido 2 numeros y los sumo
import re
import io
class SumaDeNumeros:
    # definimos una lista vacia
    def __init__(self):
        self.numerosIngresados = []


    def presentacion(self):
        print("\n\n\t\tPrograma que permite cargar dos valores por teclado.")
        print("\t\t\tEfectua la suma de los valores.")
        print("\t\t\tMuestra el resultado de la suma.")
        print("\t\t*********************************************************\n\n")


    def cargaYSuma(self):

        while True:
            try:
                num1 = int(input("ingrese el primer numero: "))
                self.numerosIngresados.append(str(num1))
                num2 = int(input("ingrese el segundo numero:"))
                self. numerosIngresados.append(str(num2))

                patron = "[0-9]+"

                if re.search(patron, str(num1)):
                    if re.search(patron, str(num2)):
                        print("La suma de los numeros es: ", num1 + num2)
                        break
            except ValueError:
                print("Alguno de los dos valores introducidos no son correctos")
                print("Intentalo de nuevo.")


    def creacionDeArchivoDeLog(self):

        file = open("Log.txt", "a")
        file.write(str(self.numerosIngresados))
        file.write("\n")
        file.close()


# programa principal
plusNumber = SumaDeNumeros()
plusNumber.presentacion()
plusNumber.cargaYSuma()
plusNumber.creacionDeArchivoDeLog()
