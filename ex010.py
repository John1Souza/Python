dinheiro = float(input('Quanto dinheiro tem pra conversão em dólar: '))
print('='*10, end=' ')
print('Considerando a cotação atual US$ 1,00 dolár vale R$ 3,27 reais', end=' ')
print('='*10)
print(f'Com R$ {dinheiro:.2f} reais você consegue comprar US$ {dinheiro/(3.27):.2f} dólares')
print('='*10, end=' ')
print('Finalizando...', end=' ')
print('='*10)