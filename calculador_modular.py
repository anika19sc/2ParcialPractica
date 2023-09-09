"""Calculadora Modular: Crea un programa que permita realizar operaciones matemáticas
básicas (suma, resta, multiplicación y división) utilizando funciones modulares para cada
operación """


num1= int(input("Ingrese numero"))
num2= int(input("Ingrese numero"))
#El programa solamente va a permitir hacer 4 operaciones básicas. 
operacion=int(input("¿Qué operación desea hacer? Presione del 1 al 4 para hacer: Suma=1, Resta=2, Multiplicación=3, División=4"));

#Función suma.
def Suma (num1, num2):
    Suma=num1+num2
    return(Suma)

#Funcion Resta.
def Resta (num1, num2):
    Resta= num1- num2
    return(Resta)

#Funcion Multiplicación.
def Multiplicar(num1,num2):
    Multiplicacion= num1 * num2
    return(Multiplicacion)

#Funcion división.
def Division(num1,num2):
    Division=num1/num2
    return(Division)

if operacion ==1:
	Suma_es= Suma (num1, num2);
	print("Resultado:", Suma_es);
elif operacion ==2:
	Resta_es= Resta (num1, num2);
	print("Resultado:", Resta_es);
elif	operacion ==3:
	Multiplicacion_es= Multiplicar (num1, num2);
	print("Resultado:", Multiplicacion_es);
elif operacion ==4:
	Division_es= Division (num1, num2);
	print("Resultado:", Division_es);
else: 
    print ("Error. Ingrese de nuevo");

