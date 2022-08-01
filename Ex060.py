import math
#n! = n . (n – 1). (n – 2). (n – 3) ... 2,1

n =int(input('Digite um número para calcular seu fatorial: '))
n1 = math.factorial(n)
print(n1)

for c in range(1, n):
    if c == 1:
        fat = n * (n - c)
        #print(c, n, fat)
    else:
        fat = fat * (n - c)
        #print(c, n, fat)
print(fat)


#n = int(input('Digite um valor: '))
#n1 = math.factorial(n)
#print(n1)
c = 1
p = n

print(f'\33[1;36m{n}! =\33[m',end=' ')
while c < n:
    #print(f'{n}! =', end=' ')
    print(f'\33[1;36m{p}\33[m', end=' ')
    print('\33[1;36m X \33[m' if p > 1 else ' = ', end=' ')
    p -= 1
    if c == 1:
        fat = n * (n - c)
    else:
        fat = fat * (n - c)
    c += 1


print(f'\33[1;36m1 = {fat}\33[m')

####CODIGO CURSO EM VIDEO

n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
f = 1
print(f'Calculando o fatorial de {n}! = ', end=' ')
while c > 0:
    print(f'{c}', end=' ')
    print(' X ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print(f)