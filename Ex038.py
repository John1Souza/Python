from time import sleep

while True:
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro: '))
    #maior = n1
    print('='*12, end=' ')
    print(f'Comparando os valores {n1} e {n2}', end=' ')
    print('='*12)
    sleep(1)
    if n2 > n1:
        print('O segundo valor é maior!')
    elif n1 > n2:
        print('O primeiro valor é maior!')
    elif n1 == n2:
        print('Não existe valor maior, os dois são \33[31miguais\33[m')
    q = input('Quer continuar? [S/N] ').upper()
    if q == 'S':
        continue
    elif q == 'N':
        break
    else:
        print('Opção inválida. tente novamente.')

