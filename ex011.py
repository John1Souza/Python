largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura *  altura
print('='*5,end=' ')
print('\33[36mCalculando a área dessa parede...\33[m ', end=' ')
print('='*5)
print(f'Essa parede tem uma área de \33[33m{area:.3f}m2\33[m')
litros = area / 2
print(f'Sendo assim, serão necessários \33[34m{litros:.4f} litros\33[m de tinta para pintá-la')
print('='*5,end=' ')
print('Finalizando... ', end=' ')
print('='*5)