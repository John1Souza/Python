for i in range(1, 6):
    peso = float(input('Digite seu peso: '))
    if i == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'O maior valor é {maior} e o menor valor {menor}')