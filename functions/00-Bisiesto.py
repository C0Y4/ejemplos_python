
#!/bin/python3
# -*- coding: utf-8 -*-

####################################
#            Functions             #       
####################################

"""
Funcion que verifica que sea un anio bisiesto
Calculos:
	1. El anio es divisible por 4, es un anio bisiesto
	2. El anio es divisible por 100 o el anio es divisible por 400. 

Anios bisiestos: 2000 - 2400 
No bisiestos: 1800 - 1900 - 2100 - 2200, 2300, 2500. 

"""

def is_leap(year):
    
    if(year%4 == 0 and year%100 != 0 or year%400 == 0):
    	return True
    else:
    	return False

year = int(input())
print(is_leap(year))



