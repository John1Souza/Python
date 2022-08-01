'''p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
print('Os 10 primeiros termos da PA são: ')

for c in range(10, 0, -1):
    a10 = p + (10 - c) * r
    print(f'{a10}', end=' ')'''

'''p = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
t = 1
a10 = ''
while t <= 10:
    a10 = p + ((t - 1) * r)
    t = t + 1
    print(a10, end=' -> ')'''


#CURSO EM VIDEO

print('Gerador de PA')
print('-='*10)
p1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = p1
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end=' ')
    termo += r
    cont += 1
print('FIM')