#coding=utf-8 

#Programa que pregunte por una hora y diga cuantos minutos representan

#Ingreso de datos

print('Este programa convierte una hora en minutos\n')
horas = input('Dame una cantidad de horas')

print('La variable horas es de tipo:', type(horas))

minutos = 60 * float(horas)
print('La variable minutos es de tipo:', type(minutos))
print('La cantidad de minutos es:', minutos)

tipo_horas = type(horas)
print('la variable tipo_horas es de tipo:', tipo_horas)


print('este programa pregunta por una hora y dice si es de día o de noche\n')
hora = int(input('Introduce una hora:'))
print('La hora ingresada fue:', hora)

#condicional
if hora <12:
    print('Es de día')
    print('Que hay de desayunar?')
elif hora == 12:
    print('Es de mediodia')
    print('Se me antoja frijolitos')

else:
     print('Es de tarde')
     print('Que rico unas cervecitas')




