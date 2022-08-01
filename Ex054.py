from datetime import date

today = date.today().year
#print(today)
maior = 0
menor = 0
for i in range(1, 8):
    ano_nasc = int(input('Digite o ano de nascimento: '))
    idade = today - ano_nasc
    if idade >= 21:
        maior+=1
    elif idade < 21:
        menor+=1
print(f'{maior} pessoas são maiores de idade e {menor} pessoas são menores de idade!')
