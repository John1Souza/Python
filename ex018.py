import math
ang = float(input('Digite o ângulo: '))
rad = math.radians(ang)
print(f'Considerando o Ângulo de {ang}º temos: ')
print(f'seu Seno é {math.sin(rad):.2f}')
print(f'Seu cosseno é {math.cos(rad):.2f}')
print(f'Sua tangente é {math.tan(rad):.2f}')
