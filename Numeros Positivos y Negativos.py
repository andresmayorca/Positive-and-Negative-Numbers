# Control if
numero = int(input('Escribe un numero: '))
if numero >0:
    print('Numero positivo')
elif numero <0:
    print('Ingrese un numero por favor positivo')
    numero = int(input('Escribe un numero: '))
else:
    print('El numero es igual cero')
    numero = int(input('Escribe un numero: '))
