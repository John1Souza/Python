from time import sleep

while True:
    reta1 = float(input('Digite a primeira reta: '))
    reta2 = float(input('Digite a segunda: '))
    reta3 = float(input('Digite a terceira: '))
    print('='*12, end=' ')
    print('Analisando triângulos...', end=' ')
    print('='*12)
    sleep(1)
    if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta3 + reta2 > reta1:
        print('Considerando os valores das retas informados, é possível formar um triângulo', end=' ')
        if reta1 == reta2 == reta3:
            print('\33[1;36mEQUILÁTERO\33[m')
        elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
            print('\33[1;32mISÓCELES\33[m')
        elif reta1 != reta2 != reta3 != reta1:
            print('\33[1;35mESCALENO\33[m')
    else:
        print('Considerando os valores das retas informados, NÃO é possível formar um triângulo.')



    q = input('Quer continuar? [S/N] ').upper()
    if q == 'S':
        continue
    else:
        break