from random import randint

cinco = (randint(0, 10), randint(0, 10), randint(0,10), randint(0,10),randint(0,10))
#print(cinco)
maior = max(cinco)
menor = min(cinco)
print('Os valores sorteados foram: ', end=' ')
for i in cinco:
    print(f'{i}', end=' ')
print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')