
reta1 = float(input('Primeira reta: '))
reta2 = float(input('Segunda reta: '))
reta3 = float(input('Terceira reta: '))
if (reta1 + reta2) > reta3 and (reta1 + reta3) > reta2 and (reta2 + reta3) > reta1:
    print(f'Os segmentos {reta1}, {reta2} e {reta3} estão dentro dos parâmetros da DESIGUALDADE TRIÂNGULAR')
else:
    print(f'Os segmentos {reta1}, {reta2} e {reta3} estão fora dos parâmetros da DESIGUALDADE TRIÂNGULAR')
print('fim')
