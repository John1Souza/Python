from time import sleep
soma = 0
for i in range(1,7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        soma += n
print(f'A soma de todos os números pares é {soma}')
