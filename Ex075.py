n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
tupla = (n1, n2, n3, n4)
print(f'Você digitou os valores {tupla}')
print(f'O número 9 apareceu um total de {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O número 3 apareceu na {tupla.index(3)+1}ª posição')
else:
    print('Não foi digitado o número 3')
print('Os números pares digitados foram: ', end=' ')
for c in range(0, len(tupla)):
    if tupla[c] % 2 == 0:
        print(f'{tupla[c]}', end=' ')