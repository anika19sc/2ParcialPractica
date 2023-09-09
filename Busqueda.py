"""Búsqueda: Escribe un programa en pseudocódigo que realice una búsqueda de un número
dado, en un arreglo. Crea una función modular para llevar a cabo la búsqueda.
"""

basta = True
numeroB = [] #Arreglo

#Ingresa numero
numero = int(input("Ingrese numero:  "))

#funcion de buscar arreglo
def busqueda_arreglo(numero):
    busqueda = (numeroB)
    return(busqueda)

while basta: #Se va a repetir nuevamente cuando basta sea 1(true)
    for i in range(basta):    #Aca seria, que basta con opcion 1 o 0 darle la finalizacion al rango del arreglo.
        numeroB.append(numero) #agregamos numero al arreglo, es decir, guardamos el numero dentro de la caja.

    numero = int(input("Ingrese numero:  "))
    basta = int(input("¿Desea seguir ingresando un numero? SI=1/ NO=0:    "))

if basta == 0: 
    busqueda=int(input("¿Desea ver algún número? Ingrese el numero que quiere buscar:    "))
    busqueda = busqueda_arreglo(numero)
    print("Se ha concretado la Busqueda de Numeros. Su valor se encuentra en algunas de las siguientes:", busqueda)
else:
    print("Error. Intente de nuevo")







