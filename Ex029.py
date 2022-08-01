vel = float(input('A quantos Km/h de velocidade estava o carro? '))
if vel > 80:
    print('ACIMA DO LIMITE!!! Multado!')
    multa = (vel-80)*7
    print(f'O valor da sua multa é de R$ {multa:.2f}')
else:
    print('Dentro do limite, próximo!')
print('='*10,end=' ')
print('Tenha um bom dia! Dirija com segurança!',end=' ')
print('='*10)
