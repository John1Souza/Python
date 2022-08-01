'''pessoas = {}
cont = soma = 0
pessoas_acima = []
mulheres = []
Nome = []
Sexo = []
Idade = []
while True:
    nome = str(input('Nome: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    if sexo not in 'MmFf':
        print('Opção inválida. Tente novamente.')
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    idade = int(input('Idade: '))
    if sexo == 'F':
        mulheres.append(nome)
    if idade > 30:
        pessoas_acima.append(nome)
    Nome.append(nome)
    Sexo.append(sexo)
    Idade.append(idade)
    cont += 1
    soma += idade
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
pessoas["nome"] = Nome
pessoas["sexo"] = Sexo
pessoas["idade"] = Idade
for j, k in enumerate(pessoas["idade"]):
    print(j, k)
print(f'- O grupo tem {cont} pessoas.')
print(f'- A média de idade é de {(soma/cont):.2f} anos.')
print(f'- As mulheres cadastradas foram: ',end='')
for i, v in enumerate(mulheres):
    print(f'{v}',end=' ')
print()
print(f'- Lista de pessoas que estão acima da média:')
for i, v in enumerate(pessoas["idade"]):
    if v > 30:
        print(f'nome = {pessoas["nome"]}; sexo = {pessoas["sexo"]}; idade = {pessoas["idade"]}')'''

galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idades é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}', end='')
        print()
print('<< ENCERRADO >>')
