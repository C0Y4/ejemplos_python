
#!/bin/python3

	####################################
	#            Tuples                #       
	####################################

""" 
Las tublas son estructuras de datos parecidas a las listas
A diferencia de las listas, las tuplas son inmutables 
(no pueden modificarse, una vez creada).
- No se puede agregar, eliminar o asignar valores.
- Un uso común de tuplas es el intercambio de 2 números:

a, b = b, a

a,b es una tupla, y se le asigna los valos a b,a

Otro uso impresionante de las tuplas es como claves en un diccionario. En otras palabras, las tuplas son hashables

"""

numeros = (5,4,3,2,1,6,45,3,6,6,6,6,6)

print (hash(numeros)) # hash

####################################################

""" 
Crear una tupla con numeros, pide un numero por teclado e indica cuantas veces se repite.

"""

numero = int(input("Ingresar un numero: "))

cont = 0
for i in numeros:
	if numero == i:
		cont = cont + 1

print ("El numero:", numero, " - cantidad: ", cont)

print ("Repeticioes del ", numero,": ", numeros.count(numero))


####################################################







