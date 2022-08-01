print('Gerador de PA')
print('-='*10)
p1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = p1
cont = 1
total = 0
q = 10
while q != 0:
    total += q
    while cont <= total:
        print(f'{termo} -> ', end=' ')
        termo += r
        cont += 1
    print('PAUSA')
    q = int(input('Quantos termos quer ver a mais? '))

print(f'Progressão finalizada com {total} termos')





