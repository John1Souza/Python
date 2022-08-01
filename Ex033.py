'''n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo: '))
n3 = int(input('Digite o terceiro: '))
if n3 < n1 > n2:
    if n2 == n3 < n1:
        print(f'{n1} é o MAIOR número!')
        print(f'{n2} é o MENOR número!')
    else:
        print(f'{n1} é o MAIOR número!')
if n3 < n2 > n1:
    if n1 == n3 < n2:
        print(f'{n2} é o MAIOR número!')
        print(f'{n1} é o MENOR número!')
    else:
        print(f'{n2} é o MAIOR número!')
if n1 < n3 > n2:
    if n1 == n2 < n3:
        print(f'{n3} é o MAIOR número!')
        print(f'{n1} é o MENOR número!')
    else:
        print(f'{n3} é o MAIOR número!')
if n1 < n2 and n1 < n3:
    if n2 == n3 > n1:
        print(f'{n2} é o MAIOR número!')
        print(f'{n1} é o MENOR número!')
    else:
        print(f'{n1} é o MENOR número!')
if n2 < n1 and n2 < n3:
    if n1 == n3 > n2:
        print(f'{n1} é o MAIOR número!')
        print(f'{n2} é o MENOR número!')
    else:
        print(f'{n2} é o MENOR número!')
if n3 < n2 and n3 < n1:
    if n1 == n2 > n3:
        print(f'{n1} é o MAIOR número!')
        print(f'{n3} é o MENOR número!')
    else:
        print(f'{n3} é o MENOR número!')
if n2 == n3 == n1:
    print(f'{n1} é o MAIOR número!')
    print(f'{n1} é o MENOR número!')

print('='*20, end=' ')
print('FIM', end=' ')
print('='*20)
'''
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b >= c:
    maior = b
if c > a and c >= b:
    maior = c
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')

