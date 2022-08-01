n = int(input('Digite um valor: '))
t1 = t3 = 0
t2 = 1
cont = 3
'''if n == 1:
    print(t1)
if n == 2:
    print(t2)'''
print(f'Os {n} primeiros termos de fibonacci são:')
print(f'{t1} {t2}', end=' ')
### FN = Fn-1 + FN-2
while cont <= n:
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        print(f'{t2}',end=' ')
        cont += 1

