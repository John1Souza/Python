pessoas = list()
dados = list()
cont = 0
pM = 0
pm = 0
while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    cont += 1
    q = input('Continuar? [S/N] ').strip().upper()[0]
    if q == 'N':
        break
    else:
        while q not in 'SnsN':
            print('Resposta inválida. Tente novamente!')
            q = input('Continuar? [S/N] ').strip().upper()[0]

pesada = []
leve = []
for p, v in enumerate(pessoas):
    if p == 0:
        pM = v[1]
        pm = v[1]
    else:
        if v[1] > pM:
            pM = v[1]
        if v[1] < pm:
            pm = v[1]
    if v[1] == pM:
        pesada.append(v[0])
    if v[1] == pm:
        leve.append(v[0])
print('=-' * 30)
print(f'Ao todo você cadastrou {cont} pessoas')###'''Dá PRA USAR O len()'''
print(f'O maior peso foi {pM:.2f} Kg. Peso de {pesada}')
print(f'O menor peso foi {pm:.2f} Kg. Peso de {leve}')


temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {mai}Kg. peso de ',end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ',end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ',end='')
print()