#1:

'''for i in range(1,11):
    n = int(input('Digite uma nota entre 0 e 10: '))
    if 0 <= n <= 10:
        break
    else:
        print('Você digitou um valor inválido. Tente novamente.')
'''

#2

'''while True:
    nome = str(input('Diga seu nome: ')).upper()
    senha = str(input('Digite uma senha: ')).upper()
    if senha in nome:
        print('Sua senha não pode se igual ao seu nome! Tente novamente.')
    else:
        print('Cadastro Aprovado.')
    p = input('Continuar? [S/N] ')
    if p in 'Ss':
        continue
    else:
        break'''
#3

while True:
    nome = input('Digite seu nome: ')
    if len(nome) < 3:
        print('Nome tem que ser maior que 3 caracteres.Tente novamente.')
        nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    if 0 > idade > 150:
        print('Idade entre 0 e 150 apenas. ')
        idade = int(input('Digite sua idade: '))
    salário = float(input('Digite seu salário: '))
    if salário < 0:
        print('Seu salário tem que ser maior do que 0: ')
    sexo = input('Digite seu sexo: [F/M] ')
    if sexo not in 'FfMm':
        print('Opção inválida. tente novamente')
        sexo = input('Digite seu sexo: ')
    estado_c = input('''Seu estado civil: 
                   [ S ] Solteiro
                   [ C ] Casado
                   [ V ] Viúvo
                   [ D ] Divorciado
                   ''')
    if estado_c not in 'SsCcVvDd':
        print('Opção inválida. tente novamente.')
        estado_c = input('''Seu estado civil: 
[ S ] Solteiro
[ C ] Casado
[ V ] Viúvo
[ D ] Divorciado
''')
    else:
        break