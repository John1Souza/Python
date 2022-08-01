viagem = float(input('Quantos Km de distância será a sua viagem? '))
if viagem <= 200:
    passagem = viagem * 0.5
    print(f'Considerando {viagem} Km de distância dessa viagem, o preço da sua passagem é R$ {passagem:.2f}')
else:
    passagem = viagem * 0.45
    print(f'Considerando que a distância de {viagem} km supera os 200 km,\n o preço da sua passagem será R$ {passagem:.2f}')
print('='*15, end=' ')
print('Obrigado por utilizar nossos serviços, tenha uma boa viagem!', end=' ')
print('='*15)