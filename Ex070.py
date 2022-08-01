q = ''
cont_maior_1000 = soma = cont = 0
while True:
    print('='*30)
    print(f'{" LOJAS SUPER -> BARATÃO ":^30}')
    print('='*30)
    nome = input('\33[1;32mNome do produto: \33[m').strip()
    preço = float(input('\33[1;33mPreço: R$ \33[m'))
    cont += 1
    soma += preço
    if preço > 1000:
        cont_maior_1000 += 1
    if cont == 1:
        menor = preço
        menor_nome = nome.capitalize()
    elif cont > 1:
        if menor > preço:
            menor = preço
            menor_nome = nome.capitalize()

    q = input('\33[1;31mContinuar? [S/N] \33[m').strip().upper()
    while q not in 'SN':
        q = input('\33[1;31mContinuar? [S/N] \33[m').strip().upper()[0]
    if q == 'N':
        break
print('-'*30)
print(f'{" FIM DO PROGRAMA ":^30}')
print('-'*30)
print(f'O total gasto foi de R$ {soma:.2f} reais')
print(f'Temos {cont_maior_1000} produtos que custam mais do que R$ 1.000,00 reais')
print(f'O é o produto mais barato foi {menor_nome} que custa R$ {menor}')