from time import sleep
print(f'{" Contagem regressiva ":=^40}')
for i in range(10, -1, -1):
    sleep(0.1)
    print(f'{i}')
    if i == 0:
        print('BOOOOOMMMMMM!!!!')

