lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    q = input('Quer continuar? [S/N] ').upper()[0]
    while q not in 'SN':
        print('Digite uma opção correta!!!')
        q = input('Quer continuar? [S/N] ').upper()[0]
    if q == 'N':
        break
print(f'Você digitou {cont} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são{lista}')
if 5 in lista:
    print('O valor 5 foi digitado e está na lista!')
else:
    print('O valor 5 não está na lista!')