aluguel = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
#o aluguel do carro custa R$ 60.00 reais por dia
#o Km rodado custa R$ 0.15 reais
print(f'O total a pagar é de R$ {(aluguel*60)+(km*0.15):.2f}')