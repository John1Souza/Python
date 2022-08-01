alunos = {}


alunos['nome'] = str(input('Nome: '))
alunos['media'] = float(input(f'Media de {alunos["nome"]}: '))
print(f'Nome é igual a {alunos["nome"]}')
print(f'Média igual a {alunos["media"]}')
if alunos["media"] <= 7:
    print(f'Situação é igual a Reprovado.')
else:
    print(f'Situação é igual a Aprovado')



######### EX 090 ######################

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperacao'
else:
    aluno['situacao'] = 'Reprovado'
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')