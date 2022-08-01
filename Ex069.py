
q = sexo = ''
qtd_mais_18 = qtd_M = qtd_F_menos_20 = 0
while q != 'N':
    print('\33[1;35m-\33[m' * 30)
    print(f"{' CADASTRE UMA PESSOA ':^30}")
    print('\33[1;35m-\33[m' * 30)
    idade = int(input('\33[1;32mIdade: \33[m'))
    sexo = input('\33[1;33mSexo: [F|M] \33[m').strip().upper()
    while sexo not in 'FM':
        sexo = input('\33[1;33mSexo: [F|M] \33[m').strip().upper()
    print('\33[1;35m-\33[m' * 30)
    if idade >= 18:
        qtd_mais_18 += 1
    if sexo == 'M':
        qtd_M += 1
    if sexo == 'F' and idade < 20:
        qtd_F_menos_20 += 1
    q = input('\33[1;31mQuer continuar? [S|N] \33[m').strip().upper()
    while q not in 'SN':
        q = input('\33[1;31mQuer continuar? [S|N] \33[m').strip().upper()
print('='*15, end=' ')
print(f'{" FIM DO PROGRAMA ":^15}', end=' ')
print('='*15)
print(f'\33[1;36mUm total de {qtd_mais_18} pessoas maiores de 18 anos.\33[M')
print(f'\33[1;36mForam cadastrados {qtd_M} homens.\33[M')
print(f'\33[1;36mUm total de {qtd_F_menos_20} mulheres tem menos de 20 anos.\33[M')