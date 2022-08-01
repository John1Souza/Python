
idade1 = media = cont =  0
for i in range(1, 5):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Qual seu sexo? [F/M] ')).upper()
    media += idade
    media_idade = media / 4
    if sexo == 'M':
        if idade > idade1:
            idade1 = idade
            nome_h = nome
            #print(f'\33[1;32m{nome_h}\33[m')
    if sexo == 'F' and idade < 20:
        cont+=1

print(f'\33[1;32mA média entre as idades é {media_idade} anos\33[m')
#print(idade1)
print(f'\33[1;35mO homem mais velho se chama {nome_h} e tem {idade1} anos\33[m')
if cont == 0:
    print('\33[1;31mNenhuma mulher tem menos de 20 anos\33[m')
else:
    print(f'\33[1;36mUm total de {cont} mulher(es) tem menos de 20 anos\33[m')