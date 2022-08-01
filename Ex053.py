print(f'{" VAMOS DESCOBRIR SE A PALAVRA É UM PALÍNDROMO ":=^60}')
p = input('Digite a frase: ').upper()
pq = p.split()
p1 = p.replace(' ', '')
inv = p1[::-1]
#print(inv)
if inv == p1:
    print(f'A frase "{p}" é um PALÍNDROMO')
else:
    print(f'A frase "{p}" não é um palíndromo')
