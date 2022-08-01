'''from time import sleep
def contador(ini, fim, pas):
    print('-='*20)
    print(f'Contagem de {ini} até {fim} de {pas}')
    while ini != 11:
        sleep(0.1)
        print(f'{ini}', end=' ')
        ini += pas
    print('FIM!')
    print('-=' * 20)
    print(f'Contagem de {fim} até {ini} de {pas+1} em {pas+1}')
    while fim >= 0:
        sleep(0.1)
        print(f'{fim}', end=' ')
        fim -= (pas+1)
    print('FIM!')
    print('-=' * 20)
    ini = int(input('Início: '))
    fim = int(input('Fim: '))
    pas = int(input('Passo: '))
    if pas < 0:
        pas1 = pas*(-1)
    if pas > 0:
        pas1=pas
    print(f'Contagem de {ini} até {fim} de {pas1} em {pas1}')
    while ini != (fim+pas):
        print(f'{ini}', end=' ')
        ini += pas
        sleep(0.5)
    print('FIM!')

# Programa Principal
contador(1, 10, 1)
'''
from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM!')



#programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print(f'Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)