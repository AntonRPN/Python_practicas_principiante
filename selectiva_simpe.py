'''
scrip en python que implemente un sistema de redondeo de 
calificaciones. El usuario es el encagado de ingresar su
calificación. Si a al calificación le faltan 4 unidades
o menos para el siguiente múltiplo de 10, entonces su calificación
será redondeada al siguiente múltiplo de 10, en ese caso contrario
la calificación no es modificada. Ejemplo:

Si el usuario obtuvo 76 entonces se redondea a 80.
Si el usuario obtuvo 77 entonces se redondea a 80
Si el usuario obtuvo 75 entonces su calificación es 75.
'''

calificacion = int(input('¿Cuál es tu calificación? '))
residuo = calificacion  % 10
mensaje = 'Tu calificación no amerita redondeo.'

if residuo >= 6:
    calificacion = calificacion + (10 - residuo)
    mensaje = f'Tu calificación es: {calificacion}'

print(mensaje) 
print('Que tengas un buen dia')