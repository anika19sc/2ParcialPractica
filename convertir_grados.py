"""Crea un programa en pseudocódigo que permita convertir entre Celsius y Fahrenheit. Crea dos funciones modulares: una para convertir de Celsius a
Fahrenheit y otra para convertir de Fahrenheit a Celsius"""

numero = int(input("Ingrese el número que desea convertir en Grado: "))
opcion = int(input("Si desea convertir el número ingresado de Celsius a Fahrenheit, presione 1. Si desea convertir de Fahrenheit a Celsius, presione 0: "))

#Funcion para convertir de grados Celsius a Fahrenheit.
def ConvertirCaF(numero):
    if opcion == 1:
        OperacionCaF = (numero * 9/5) + 32
        return OperacionCaF

#Función para convertir de grados Fahrenheit a Celsius.
def ConvertirFaC(numero):
    if opcion == 0:
        OperacionFaC = (numero - 32) * 5/9
        return OperacionFaC 
    
#Si la persona coloca la opción, lo que pasará es que va a convertir el numero en grados f.

if opcion == 1:
    Mostrar = ConvertirCaF(numero) #Muestra la función.
    print("El resultado es", Mostrar)

elif opcion == 0:  #Por ende, si la persona coloca la opción 0 convertirá el grado de F a Celsius.
    Mostrar = ConvertirFaC(numero)
    print("Su resultado es", Mostrar)
else:
    print("Número Incorrecto.")
