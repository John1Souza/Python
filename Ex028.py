from random import randint
from time import sleep
computador = randint(0, 5)
print('\33[36m=\33[m'*20, end=' ')
print('\33[36mESTOU PENSANDO EM UM NÚMERO ENTRE 0 E 5...TENTE ADVINHAR\33[m', end=' ')
print('\33[36m=\33[m'*20)
n1 = int(input('Em que núemro eu pensei? '))
print('\33[33mProcessando...\33[m')
sleep(2)
if computador == n1:
    print('PARABENS!!! Você venceu!')
else:
    print('PERDEU!!! Mais sorte na próxima!')
print('\33[36m=\33[m'*20, end=' ')
print('\33[36mFIM\33[m', end=' ')
print('\33[36m=\33[m'*20)