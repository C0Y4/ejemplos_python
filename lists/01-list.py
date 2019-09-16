#!/bin/python3
# -*- coding: utf-8 -*-

####################################
#            Lists                 #       
####################################

"""Dada una lista. Realizar las siguientes operaciones:
	
	1. Agregar un elemento a la lista (un entero) en la posicion i - insert
	2. print list. Muestra la lista.
	3. Eliminar la primera ocurrencia de un entero n - remove
	4. Insertar un elemento al final de la lista - append
	5. Ordenar lista - sort
	6. Sacar el ultimo elemento de la lista 
	7. Revertir elementos de la lista - reverse


Ejemplo input: 

	12
	insert 0 5
	insert 1 10
	insert 0 6
	print
	remove 6
	append 9
	append 1
	sort
	print
	pop
	reverse
	print



"""

if __name__ == '__main__':

    N = int(input())   

    result = []

    for n in range(N):

        x = input().split(" ")
        command = x[0]
        print (x)
        if command == 'append':
            result.append(int(x[1]))
        if command == 'print':
            print(result)
        if command == 'insert':
            result.insert(int(x[1]), int(x[2]))
        if command == 'reverse':
            result = result[::-1]
        if command == 'pop':
            result.pop()
        if command == 'sort':
            result = sorted(result)
        if command == 'remove':
            result.remove(int(x[1]))


""" output 

    [6, 5, 10]

    [1, 5, 9, 10]

    [9, 5, 1]


"""
