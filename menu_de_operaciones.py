SUMA = 1
RESTA = 2
MULTIPLICACION = 3
DIVISION = 4
DIVISION_ENTERA = 5
MODULO = 6
POTENCIA = 7

print(f'''        Calculadora

{SUMA} Suma
{RESTA} Resta
{MULTIPLICACION} Multiplicación
{DIVISION} División
{DIVISION_ENTERA} División Entera
{MODULO} Módulo
{POTENCIA} Potencia

''')

opc = int(input('Elige una opción: '))

if SUMA <= opc <= POTENCIA:
    primer = int(input('Primer operando: '))
    segundo = int(input('Segundo operando: '))
    if opc == SUMA:
        print(f'{primer} + {segundo} = {primer+segundo}')
    elif opc == RESTA:
        print(f'{primer} - {segundo} = {primer-segundo}')
    elif opc == MULTIPLICACION:
        print(f'{primer} * {segundo} = {primer*segundo} ')
    elif opc == DIVISION:
        if segundo != 0:
            print(f'{primer} / {segundo} = {primer/segundo} ')
        else:
            print('Operación no definida')
    elif opc == DIVISION_ENTERA:
        if segundo != 0:
            print(f'{primer} // {segundo} = {primer//segundo} ')
        else:
            print('Operación no definida')
    elif opc == MODULO:
        if segundo != 0:
            print(f'{primer} % {segundo} = {primer%segundo} ')
        else:
            print('Operación no definida') 
    else:
        print(f'{primer} ** {segundo} = {primer**segundo} ')


else:
    print('Opción no válida')

print('Nos vemos')
