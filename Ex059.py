n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
opção = ''
soma = mult = Maior = 0
while opção != 5:
    print('''-------- OPÇÕES DE OPERAÇÕES --------
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opção = int(input('Qual a operação desejada? '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma dos valores {n1} e {n2} é {soma}')
    elif opção == 2:
        mult = n1 * n2
        print(f'A multiplicação dos valores {n1} e {n2} é {mult}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
            print(f'O maior valor digitado é {maior}')
        elif n2 > n1:
            maior = n2
            print(f'O maior valor digitado é {maior}')
    elif opção == 4:
        n1 = int(input('Digite outro valor: '))
        n2 = int(input('Digite outro: '))
    else:
        print('Opção inválida. Tente novamente.')
print('Fim')
