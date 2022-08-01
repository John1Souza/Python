from time import sleep

while True:
    altura = float(input('Digite a sua altura: '))
    peso = float(input('Digite seu peso: '))
    IMC = peso / ((altura)**2)
    if IMC < 18.5:
        print(f'Considerando seu IMC {IMC:.2f} kg/m2 você está \33[1;31mABAIXO DO PESO\33[m')
    elif 18.5 <= IMC < 25:
        print(f'Considerando seu IMC {IMC:.2f} kg/m2 você está no \33[1;32mPESO IDEAL\33[m')
    elif 25 <= IMC < 30:
        print(f'Considerando seu IMC {IMC:.2f} kg/m2 você está \33[1;34mACIMA DO PESO\33[m')
    elif 30 <= IMC < 40:
        print(f'Considerando seu IMC {IMC:.2f} kg/m2 você está em \33[1;33mOBESIDADE\33[m')
    elif IMC >= 40:
        print(f'Considerando seu IMC {IMC:.2f} kg/m2 você está em estado de \33[1;31mOBESIDADE MÓRBIDA\33[m')


    q = input('Quer continuar? [S/N] ').upper()
    if q == 'S':
        continue
    else:
        break