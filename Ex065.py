q = ''
soma = cont = 0
while q != 'N':
    n = int(input('Digite um valor: '))
    soma+=n
    cont+=1
    if cont == 1:
        maior = menor = n
    else:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
    q = input('Quer continuar? [S/N] ').upper()
print(f'A média entre os {cont} valores é {soma/cont:.2f}')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}')

