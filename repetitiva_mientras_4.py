'''
Scrip en Python que muestre un menú con distintos personajes de un 
videojuego. Si el usuario selecciona alguno de los érsonajes, se le 
mostrarán sus características. el menú será cíclico y se mostrará
mientras el usuario no indique que desea salir.
'''

import os

def run():
    MAGO = 1
    GUERRERO = 2
    SACERDOTISA = 3
    SALIR = 4

    #bandera
    continuar = True

    while continuar:
        os.system('clear')
        print(f'''
        {MAGO}) Mago
        {GUERRERO}) Guerrero
        {SACERDOTISA}) Sacerdotisa
        {SALIR}) Salir
        ''')
        opc = int(input('Slecciona tu personaje: '))

        if opc == MAGO:
            print('''
            Fuerza: 15
            Energía: 20
            Especial: 12
            ''')
        elif opc == GUERRERO:
            print('''
            Fuerza: 25
            Energía: 18
            Especial: 10
            ''')
        elif opc == SACERDOTISA:
            print('''
            Fuerza: 18
            Enegía: 25
            Especial: 22
            ''')
        elif opc == SALIR:
            continuar = False
        else:
            print('Opción no válida')
        input('Presiona enter para continuar ')
    
    print('Nos vemos...')

if __name__ == "__main__":
    run()