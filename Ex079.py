val = []
while True:
    n = int(input('Digite um valor: '))
    if n not in val:
        val.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    q = input('Continuar? [S/N] ').upper()[0]
    while q not in 'SN':
        q = input('Opção inválida!!! Para continuar tecle: [S/N] ').upper()[0]
    if q == 'N':
        break
print('=-'*30)
val.sort()
print(f'Você digitou os valores {val}')
