'''from datetime import date
time = date.today().year

CTPS = dict()

CTPS["nome"] = str(input('Nome: '))
CTPS["Ano"] = int(input('Ano de nascimento: '))
CTPS["ctps"] = int(input('Carteria de Trabalho (0 não tem): '))
if CTPS["ctps"] != 0:
    CTPS["contratação"] = int(input('Ano de contratação: '))
    CTPS["salário"] = float(input('Salário R$: '))
    ano_aposentadoria = CTPS["contratação"] + 35
    idade_contratação = (time - CTPS["Ano"]) - (time - CTPS["contratação"])
    idade_aposentar = idade_contratação + 35


idade = time-CTPS["Ano"]
print(f'Nome tem o valor {CTPS["nome"]}')
print(f'Idade tem o valor {idade}')
print(f'CTPS tem o valor {CTPS["ctps"]}')
if CTPS["ctps"] != 0:
        print(f'Contratação tem o valor {CTPS["contratação"]}')
        print(f'Salário tem o valor {CTPS["salário"]}')
        print(f'Aposentadoria tem o valor {idade_aposentar}')'''
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] =dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print('=-'*30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
