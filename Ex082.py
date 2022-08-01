lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    q = input('Quer continuar? [S/N] ').upper()[0]
    while q not in 'SsNn':
        print('Opção inválida. Tente novamente! ')
        q = input('Quer continuar? [S/N] ').upper()[0]
    if q == 'N':
        break
par = []
impar = []
for c, v in enumerate(lista):
    if v % 2 == 0:
        par.append(lista[c])
    elif v % 2 != 0:
        impar.append(lista[c])
print('=-' * 30)
print(f'A Lista criada é : {lista}')
print(f'A lista de valores pares é: {par}')
print(f'A lista de valores impares é: {impar}')
