sal = float(input('Qual o salário do funcionário? R$ '))
if sal <= 1250:
    reajuste = sal * 1.15
    print(f'Seu salário atual é de R$ {sal:.2f}, com o reajuste passa a ser R$ {reajuste:.2f}')
else:
    reajuste = sal * 1.10
    print(f'O salário atual é de R$ {sal:.2f}, com o reajuste passa a ser R$ {reajuste:.2f}')
print('-'*15, end=' ')
print('FIM', end=' ')
print('-'*15)