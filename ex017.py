import math
catO = float(input('Digite o cateto oposto: '))
catA = float(input('Digite o cateto adjacente: '))
print(f'Considerando o cateto oposto e adjacente informados {catO} e {catA},\na hipotenusa correspondente é {math.hypot(catO, catA):.4f}')