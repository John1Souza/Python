'''n = int(input('Digite um valor entre 0 e 9999: '))
print(f'Analisando o número {n}')
u = n % 10
print(f'unidade: {u}')
d = n % 100
d1 = d // 10
print(f'dezena: {d1}' )
c = n % 1000
c1 = c // 100
print(f'centena: {c1}')
m = n // 1000
print(f'milhar{m}')'''
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}')
print(f'Unidade: {u}')
print(f'Unidade: {d}')
print(f'Unidade: {c}')
print(f'Unidade: {m}')

