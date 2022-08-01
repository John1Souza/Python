from time import sleep
from random import randint


while True:
    jokenpo = ['Pedra', 'Papel', 'Tesoura']
    computador = randint(1, 3)
    #print(computador)
    #1 == pedra
    #2 == papel
    #3 == tesoura
    if computador == 1:
        comp = jokenpo[0]
    elif computador == 2:
        comp = jokenpo[1]
    elif computador == 3:
        comp = jokenpo[2]
    comp = comp.upper()
    JoKenPô = input('Pedra, Papel ou Tesoura: ').upper()
    print('='*15,end=' ')
    sleep(0.5)
    print('Jo,', end=' ')
    sleep(0.5)
    print('Ken,', end=' ')
    sleep(0.5)
    print('Pô', end=' ')
    sleep(0.5)
    print('='*15)
    if JoKenPô == 'PEDRA' and comp == 'PEDRA' or JoKenPô == 'PAPEL' and comp == 'PAPEL' or JoKenPô == 'TESOURA' and comp == 'TESOURA':
        print('\33[1;36mEmpate!!!\33[m')
    elif JoKenPô == 'PEDRA' and comp == 'PAPEL' or JoKenPô == 'PAPEL' and comp == 'TESOURA' or JoKenPô == 'TESOURA' and comp == 'PEDRA':
        print(f'\33[1;31mPERDEU!!!\33[m Você escolheu \33[1;32m{JoKenPô}\33[m e o computador \33[1;35m{comp}\33[m')
    elif JoKenPô == 'PAPEL' and comp == 'PEDRA' or JoKenPô == 'PEDRA' and comp == 'TESOURA' or JoKenPô == 'TESOURA' and comp == 'PAPEL':
        print(f'\33[1;36mVENCEU!!!\33[m Você escolheu \33[1;32m{JoKenPô}\33[m e o computador \33[1;35m{comp}\33[m')
    else:
        print('OPÇÃO INVÁLIDA. Tente novamente.')

    q = input('Quer continuar? [S/N] ').upper()
    if q == 'S':
        continue
    else:
        break