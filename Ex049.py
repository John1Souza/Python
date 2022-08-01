from time import sleep

print(f'{" VAMOS CALCULAR A TABUADA ":=^40}')
n = int(input('Digite um número? '))
print(f'A tabuada do número {n} é: ')
for i in range(1, 11):
      sleep(1)
      print(f'\33[1;32m{n}\33[m X \33[1;34m{i:2}\33[m = \33[1;36m{n*i:2}\33[m')
