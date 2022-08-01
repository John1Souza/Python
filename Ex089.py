aluno = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    a = [nome]
    a1 = [nota1, nota2]
    a2 = [a, a1]
    aluno.append(a2)
    q = input('Quer continuar? [S/N] ')
    if q in 'Nn':
        break
    while q not in 'SsNn':
        print('Resposta inválida. Tente novamente.')
        q = input('Quer continuar? [S/N] ')
print(aluno)
print('=-'*45)
print(f'{"No.":<5}{"NOME":<15}{"MEDIA":<15}')
print('-'*30)
for i in aluno:
    soma = i[1][0] + i[1][1]
    print(f'{aluno.index(i):<5}{i[0][0]:<15}{soma: <15.2f}')
print('-'*30)
r = 0
while r != 999:
    r = int(input('Mostrar a nota de qual aluno? (999 interrompe): '))
    for j in aluno:
        if r == aluno.index(j):
            print(f'As notas de {j[0][0]} são {j[1]}')
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"nome":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')