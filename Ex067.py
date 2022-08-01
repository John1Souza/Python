n = 0
c = 1
while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    print('\33[1;36m=\33[m' * 37)
    if n < 0:
        break
    while c <= 10:
        print(f'\33[1;35m{n:2} X {c:2} = {n*c:2}\33[m')
        c += 1
    c = 1
    print('\33[1;36m=\33[m' * 37)