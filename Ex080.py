''''num = []
M = m = 0
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if i == 0:
        M = m = n
        num.append(n)
    else:
        if n > M:
            M = n
            num.append(n)
        if n < m:
            m = n
            num.insert(0, n)
    q = input('Continuar? [S/N] ')
    while q not in 'SsNn':
        print('Resposta inválida!! Tente novamente.')
        q = input('Continuar? [S/N] ').strip().upper()[0]
    if q in 'Nn':
        break
print(num)
print(M,m)'''

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('=-' * 30)
print(f'Os valores digitados em ordem foram {lista}')


