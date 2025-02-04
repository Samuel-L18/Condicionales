#coding=utf-8

#Progrma para demostrar condicionales compuestos 
# Utilizando if-else y los operadores lógicos and y or 
#Se pide la edad al usuario
#Se pide la nacionalidad al usuario
#Si es colombiano y tiene edad mayor o igual a 18 años, puede votar
#Si es extrangero y tiene edad mayor o igual a 21 años, puede votar 

print ('Programa para demostrar condicionales compuestis')
print('Utilizando if-else y los operadores lógicos and y or')

edad= int(input('Ingrese su edad:'))
nacionalidad= input('Ingrese su nacionalidad:').lower()

if nacionalidad == 'colombiano' and edad >= 18:
    print('Eres colombiano y mayor de edad, puedes votar')

if nacionalidad == 'extrangero' and edad >= 21:
    print('Eres extrangero y mayor de edad, puedes votar')

if nacionalidad == 'colombiano' and edad < 18:
    print('Eres colombiano y menor de edad, no puedes votar')

if nacionalidad == 'extrangero' and edad < 21:
    print('Eres extrangero y menor de edad, no puedes votar')
