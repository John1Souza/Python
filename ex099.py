from time import sleep


def maior(*valor):
    print('-='*30)
    cont = maior = 0
    print('Analisando os valores passados...')
    for i in valor:
        print(f'{i} ', end='')
        sleep(0.5)
        if cont == 0:
            maior = i
        else:
            if i > maior:
                maior = i
        cont += 1
    sleep(0.5)
    print(f'Foram informados {cont} valores ao todo.')
    sleep(0.5)
    print(f'O maior valor informado foi {maior}')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
#maior()
