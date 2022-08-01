'''a1 = []
for i in range(0, 3):
    n = int(input(f'Digite um valor para [0, {i}]: '))
    a1.append(n)
for c in range(0, 3):
    n = int(input(f'Digite um valor para [1, {i}]: '))
    a1.append(n)
for p in range(0, 3):
    n = int(input(f'Digite um valor para [2, {i}]: '))
    a1.append(n)
print('=-'*30)
mont = 0
soma=0
soma3 = 0
for i in a1:
    print(f'[ {i} ]', end='')
    mont+=1
    if mont == 3:
        soma3+=i
        print('\n',end='')
        mont = 0
    if i % 2 == 0:
        soma+=i
m = 0
for j in a1[3:6]:
    m = a1[3]
    if a1[4] > m:
        m = a1[4]
    if a1[5] > m:
        m = a1[5]
print('=-'*10,end='')
print(f'{" DESAFIO APRIMORADO ":>15}',end='')
print('=-'*10)
print(f'\33[34mA soma de todos os valores pares é: {soma}\33[m')
print(f'\33[35mA soma de todos os valores da terceira coluna é: {soma3}\33[m')
print(f'\33[33mO maior valor da segunda coluna é: {m}\33[m')'''
matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor par [{l}, {c}]: '))
print('=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(o, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')