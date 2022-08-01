numero = ('zero','um', 'dois', 'três', 'quatro', 'cinco'
          , 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
          'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
          'dezessete', 'dezoito', 'dezenove', 'vinte')
n = 0

while True:
    n = int(input('Tente novamente.Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        q = str(input('Continuar? [S/N] ')).upper()[0]
        if q == 'N':
            break
print(f'Você digitou o número {numero[n]}')
