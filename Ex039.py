from datetime import date
while True:
    ano_atual = date.today().year
    ano_nasc = int(input('Digite o ano do seu nascimento: '))
    sexo = input('Qual seu sexo? [M/F] ').upper()
    if sexo == 'M':
        if (ano_atual-ano_nasc) < 18:
            print(f'Você ainda tem {ano_atual-ano_nasc} anos, faltam {18-(ano_atual-ano_nasc)} anos para poder se alistar!')
            ano_alist = (18-(ano_atual-ano_nasc)) + ano_nasc
            print(f'Seu alistamento será em {ano_alist}')
        elif (ano_atual-ano_nasc) == 18:
            print(f'Você tem {ano_atual-ano_nasc} anos, está na hora de se alistar!')
        elif (ano_atual-ano_nasc) > 18:
            print(f'Você tem {ano_atual-ano_nasc} anos, \33[33mjá passou {(ano_atual-ano_nasc)-18} anos do seu tempo de alistamento\33[m')
            print(f'O ano do seu alistamento foi {ano_atual-((ano_atual-ano_nasc)-18)}')
    elif sexo == 'F':
        print('Você não é obrigada a se alistar!')
    else:
        print('Opção inválida.')
    q = input('Quer continuar? [S/N] ').upper()
    if q == 'S':
        continue
    else:
        break