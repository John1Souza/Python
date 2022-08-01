print(f'{" CALCULANDO NÚMEROS PRIMOS ":=^40}')

while True:

    n = int(input('Digite um número: '))
    divisor = 0
    for c in range(1, n+1):
        #d = n % c
        if n % c == 0:
            divisor+=1
        '''elif d != 0:
            divisor += 0'''
    if divisor == 2:
        print(f'\33[1;36m{n}\33[m \33[1;32mé um número primo\33[m')
    else:
        print(f'\33[1;36m{n}\33[m \33[1;31mNão é um número primo\33[m')


    q = input('Quer continuar? [S/N] ').upper()
    if q == 'S':
        continue
    else:
        break