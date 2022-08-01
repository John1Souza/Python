print(f'{" VAMOS CALCULAR A P.A. ":=^40}')
p1 = int(input('Digite o primeiro termo dessa P.A.: '))
R = int(input('Digite a razão dessa P.A.: '))
for c in range(1, 11):
    An = p1 + ((c - 1) * R)
    print(f'{An}', end=' -> ' )