from datetime import date

while True:
    ano_atual = date.today().year
    ano_nasc = int(input('Digite o ano de nascimento do atleta: '))
    idade = ano_atual - ano_nasc
    if idade <= 9:
        print(f'Considerando a sua idade de {idade} anos, sua categoria é \33[32mMIRIM\33[m')
    elif idade <= 14:
        print(f'Considerando sua idade de {idade} anos, sua categoria é \33[1;33mINFANTIL\33[m')
    elif idade <= 19:
        print(f'Considerando sua idade de {idade} anos, sua categoria é \33[1;34mJUNIOR\33[m')
    elif idade <= 20:
        print(f'Considerando sua idade de {idade} anos, sua categoria é \33[1;35mSÊNIOR\33[m')
    elif 20 < idade:
        print(f'Considerando sua idade de {idade} anos, sua categoria é \33[1;36mMASTER\33[m')


    q = input('Quer continuar? [S/N] ').upper()
    if q == 'S':
        continue
    else:
        break