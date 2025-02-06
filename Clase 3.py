#coding=utf-8

#Programa para imprimir números del 1 al 10

print('Programa para imprimir número del 1 al 10')

#Partes de un ciclo de control
# 1. Inicialización de la variable de control
# 2. Condición de repetición 
# 3. Sentencia de salida 

# Primer arbolito: ladeado a la izquierda, de menor a mayor

print('Primer arbolito: ladeado a la izquierda, de menor a mayor')
nivel = 1
while nivel <= 10:
    print(nivel * '*')
    nivel += 1

print('Segundo arbolito: ladeado a la izquierda, de menos a mayor')

nivel = 10
while nivel >= 1:
    print(nivel * '*')
    nivel -= 1

print('\nTercer arbolito: ladeado a la derecha, de menor a mayor')        

total_niveles = 10
cantidad_espacios = total_niveles - 1
nivel = 1
while nivel <= total_niveles:
    print('' * cantidad_espacios + nivel * '*')
    nivel += 1
    cantidad_espacios -= 1
    