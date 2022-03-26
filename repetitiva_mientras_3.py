'''
Scrip en Python que simule el sistema de validación de datos de una
plataforma digital. Se le solicitará al usuario su nombre y 
contraseña mientras la información proporcionada no coincidacon la 
infromación previamente registrada.
'''
import os

def run():

    USER = 'pepe_nava'
    PASSWORD = 'v1dr1o'

    user = ''
    password = ''

    while USER != user or PASSWORD != password:
        os.system('clear')
        print('                 kit-kot')
        user = input('Usuario: ')
        password = input('Contraseña: ')

        if USER != user or PASSWORD != password:
            print('Credenciales incorrectas')
            print('Intenta de nuevo')
            input('Presiona enter para continuar ')
    else:
        print('Bienvenid@')
    
    print('Nos vemos ....')




if __name__ == "__main__":
    run()