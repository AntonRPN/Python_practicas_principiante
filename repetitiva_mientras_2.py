'''
Script en Python que sume valores y multiplique valores impares
mientras el usuario no ingrese 0. Se deberá utilizar la estructura
repetitiva "mientras" para solicitar al usuario un número y 
dependiendo del número lo suma o lo multiplica.
'''

print('Programa que suma los números pares y multiplique los impares')
suma = 0
multiplicacion = 1
numero = -1

while numero != 0:
    numero = int(input('Ingresa un número (0 para salir): '))
    if numero % 2 == 0:
        suma = suma + numero
    else:
        multiplicacion = multiplicacion * numero
    
    print(f'suma: {suma} ')
    print(f'multiplicación: {multiplicacion} ')

print('Nos vemos')