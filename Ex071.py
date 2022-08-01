print('-='*15)
print(f'{" BEM VINDO AO CAIXA ELETRÔNICO ":^15}')
print('-='*15)
valor = int(input('Quanto deseja sacar meu nobre? R$ '))
d_1 = d_10 = d_20 = d_50 = c_1 = c_10 = c_20 = c_50 = r_1 = r_10 = r_20 = r_50 = 0
print('Essas são as opções de saque...')
while d_50 <= 1:
    c_50 = valor // 50
    r_50 = valor % 50
    #d_50 += 1
    #print(f'\33[1;32m{c_50}, {d_50},{r_50}\33[m')
    if r_50 != 0:
        c_20 = r_50 // 20
        r_20 = r_50 % 20
        #d_20 += 1
        #print(f'\33[1;31m{c_20}, {d_20},{r_20}\33[m')
        if r_20 != 0:
            c_10 = r_20 // 10
            r_10 = r_20 % 10
            #d_10 += 1
            #print(f'\33[1;33m{c_10}, {d_10},{r_10}\33[m')
            if r_10 != 0:
                r_1 = r_10 % 1
                c_1 = r_10 // 1
                #d_1 += 1
                #print(f'\33[1;34m{c_1}, {d_1},{r_1}\33[m')
            elif r_10 == 0:
                break
        elif r_20 == 0:
            break
    elif r_50 == 0:
        break
if c_50 != 0:
    print(f'Total de {c_50} cédulas de R$ 50,00')
if c_20 != 0:
    print(f'Total de {c_20} cédulas de R$ 20,00')
if c_10 != 0:
    print(f"Total de {c_10} cédulas de R$ 10,00")
if c_1 != 0:
    print(f"Total de {c_1} cédulas de R$ 1,00")



###CURSO EM VIDEO

print('='*30)
print(f'{" BANCO CEV ":^30}')
print('='*30)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R$ {céd}')
        if céd == 50:
            céd == 20
        elif céd == 20:
            céd == 10
        elif céd == 10:
            céd == 1
        totcéd = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre BANCO CEV! Tenha um bom dia!' )

