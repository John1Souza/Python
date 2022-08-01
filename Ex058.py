from random import randint
comp = randint(0, 10)
print('\33[1;36mSou seu computador...Acabei de pensar em um número entre 0 e 10.\33[m')
print('\33[1;36mTente advinhar qual foi...\33[m')
n = ''
cont = 0
#print(comp)
while comp != n:
    n = int(input('\33[1;35mQual seu palpite? \33[m'))
    cont+=1
    if comp > n:
        print('\33[1;31mMais...tente novamente!\33[m')
    elif comp < n:
        print('\33[1;33mMenos...Tente novamente.\33[m')
print(f'\33[1;32mVocê acertou!!! Levou um total de {cont} tentativas\33[m')

