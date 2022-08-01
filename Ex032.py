'''while True:
    ano = int(input('Qual o ano? '))
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                print(f'\33[33m{ano} é um ano BISSEXTO!\33[m')
            if ano % 400 != 0:
                print(f'\33[34m{ano} NÃO é um ano BISSEXTO!\33[m')
        else:
            print(f'\33[35m{ano} é um ano BISSEXTO!\33[m')
    else:
        print(f'\33[36m{ano} NÃO é um ano BISSEXTO!\33[m')
    q = input('Continuar? [S/N] ').upper()
    if q == 'S':
        continue
    else:
        break
print('FIM')'''
from datetime import date

ano = int(input('Que ano quer analisar? Aperte 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\33[33m{ano} é um ano BISSEXTO!\33[m')
else:
    print(f'\33[36m{ano} NÃO é um ano BISSEXTO!\33[m')



