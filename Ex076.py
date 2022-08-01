lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
         'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*40)
print(f'{" LISTAGEM DE PREÇOS ":^40}')
print('-'*40)
#produto = ''
#valor = 1

for c in lista:
    if type(c) == str:
        produto = c
        print(f'{produto:.<30}R$', end=' ')
    elif type(c) == float:
        val = c
        print(f'{val: >6.2f}')
print('-'*40)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end=' ')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-'*40)