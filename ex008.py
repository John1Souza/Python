n = float(input('Quantos metros serão convertidos: '))
#centimetros = n * 100
#milimetros = n * 1000
print(f'A medida de {n}m corresponde a:  ')
print(f'{n/1000:.3f}km')
print(f'{n/100:.2f}hm')
print(f'{n/10:.1f}dam')
print(f'{n*10:.0f}dm')
print(f'{n*100:.0f}cm')
print(f'{n*1000:.0f}mm')