"""Números Primos en un Rango: Escribe un programa en pseudocódigo que encuentre y
muestre todos los números primos dentro de un rango dado. Utiliza una función modular
para determinar si un número es primo."""

#Función para calcular el numero ingresado por el usuario.
def calcular(numero):
    contador = 0
    for dividendo in range(1, numero + 1):  
        if numero % dividendo == 0:
            contador += 1
            
    if contador == 2:
        return "Es primo"
    else:
        return "No es primo"

seguir = 1
while seguir == 1:
    numero = int(input("Ingrese un número: "))
    resultado = calcular(numero)
    print("Mostrar todos los números primos:", resultado)
    seguir = int(input("¿Desea seguir ingresando números? Si=1 / No=0: "))
