while True:
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda: '))
    média = (nota1 + nota2) / 2
    if média < 5.0:
        print(f'\33[1;31mREPROVADO!!!\33[m Sua média final foi \33[31m{média}\33[m')
    elif 6.9 >= média >= 5.0:
        print(f'\33[1;33mRECUPERAÇÃO!!!\33[m Sua média final foi \33[33m{média}\33[m')
    elif média >= 7.0:
        print(f'\33[1;32mAPROVADO!!!\33[m Sua média final foi \33[32m{média}\33[m')

    q = input('Quer continuar? [S/N] ').upper()
    if q == 'S':
        continue
    else:
        break