'''
scrip en python que solicite al usuario intente adivinar un número
entre el 1 y 10. Si el usuario lo adivina entonces lo felicita por
su logro; en caso contrario le indica cual era el número secreto.
'''

import random

secreto = random.randint(1, 10)
print('Acabo de generar un número secreto entre 1 y 10.')
usuario = int(input('¿Cuál crees que sea mi numero secreto? '))

if usuario == secreto:
    print('Logro desbloqueado: Adivin@ místic@')
else:
    print(f'Mi número secreto era {secreto}')

print('Que tengas un buen día')