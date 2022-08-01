n = cont = soma = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        cont+=1
        soma+=n
print(f'Foram digitados {cont} valores e a soma deles é {soma}')

