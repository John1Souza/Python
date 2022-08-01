from time import sleep

while True:
    produto = float(input('Digite o valor do produto: '))
    print('Qual será a forma de pagamento?\n'
          '[1] Dinheiro/Cheque\n'
          '[2] Cartão à vista\n'
          '[3] Até 2x no cartão\n'
          '[4] 3x ou mais no cartão')
    p = int(input('Qual a opção escolhida: '))
    if p == 1:
        print('='*10, end=' ')
        print('Analisando...', end=' ')
        print('='*10)
        sleep(0.5)
        print('A opção escolhida foi Dinheiro/Cheque')
        sleep(0.5)
        print('Para essa opção há um desconto de 10% sobre o valor do produto.')
        sleep(1)
        print(f'Sendo assim, o valor final do seu produto é de R$ {(produto*0.9):.2f}')
    elif p == 2:
        print('=' * 10, end=' ')
        print('Analisando...', end=' ')
        print('=' * 10)
        sleep(0.5)
        print('A opção escolhida foi Cartão à vista')
        sleep(0.5)
        print('Para essa opção há um desconto de 5% sobre o valor do produto.')
        sleep(1)
        print(f'Sendo assim, o valor final do seu produto é de R$ {(produto * 0.95):.2f}')
    elif p == 3:
        print('=' * 10, end=' ')
        print('Analisando...', end=' ')
        print('=' * 10)
        sleep(0.5)
        print('A opção escolhida foi Cartão em até 2x')
        sleep(0.5)
        print('Para essa opção não há desconto sobre o valor do produto.')
        sleep(1)
        print(f'Sendo assim, o valor final do seu produto é de R$ {(produto):.2f} em até 2x')
    elif p == 4:
        print('=' * 10, end=' ')
        print('Analisando...', end=' ')
        print('=' * 10)
        sleep(0.5)
        print('A opção escolhida foi Cartão em 3x ou mais')
        sleep(0.5)
        print('Para essa opção há juros de 20,00% sobre o valor do produto.')
        sleep(1)
        print(f'Sendo assim, o valor final do seu produto é de R$ {(produto*1.2):.2f} em 3x ou mais')
    q = input('Quer continuar? [S/N] ').upper()
    if q == 'S':
        continue
    else:
        break