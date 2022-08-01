lista = [[], []]
n = 0
for i in range(0, 7):
    n = int(input(f'Digite o {i+1}º valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    if n % 2 != 0:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitados foram: {lista[1]}')
