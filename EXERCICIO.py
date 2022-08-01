'''while True:
    n = int(input('Digite um valor entre 0 e 1000: '))
    u = n % 10
    d = n % 100 // 10
    c = n // 100
    print(f'{u} unidades')
    print(f'{d} dezenas')
    print(f'{c} centenas')
    q = input('Quer continuar? [S/N] ').upper()
    if q == 'S':
        continue
    else:
        break'''

#Ex 046
###FOGOS DE ARTIFICIO DE 10 A 0 COM 1 SEG DE ESPERA
'''from time import sleep
for cont in range(11, -1, -1):
    print(cont)
    sleep(0.5)
print('BUM! BUM! POOOOWWW!!!')'''
#Ex 047
#CONTAGEM DE TODOS OS NUMEROS PARES DE 1 A 50
'''for num in range(2, 51, 2):
    #if num % 2 == 0:
    print(num, end=' ')
print('Acabou')'''

#Ex 048
#SOMA ENTRE OS VALORES MULTIPLOS DE 3 NO ENTRE 1 E 500
'''soma = 0
cont = 0
for i in range(3, 501, 3):
    if i % 2 != 0:
        #print(i)
        soma += i
        cont += 1
print(soma, cont)'''
'''soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'A soma de todos os {cont} valores solicitados é {soma}')'''

#Ex 049
#TABUADA
'''n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{n:2} X {c:2} = {n*c:2}')'''


#Ex 050
#SOMA DE PARES
'''soma = 0
cont = 0
for c in range(1,7):
    n = int(input(f'Digite o {c} valor: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Você digitou {cont} números pares e a soma deles foi {soma}')'''

#Ex 051
#10 termos de uma P.A.
'''primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 -1) * razão
for c in range(primeiro, décimo + razão, razão):
    print(f'{c}', end=' -> ')'''
#Ex 052
#NUMEROS PRIMOS OU NÃO
'''núm = int(input('Digite um número: '))
cont = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        cont += 1
        print('\033[33m', end= '')
    else:
        print('\033[31m', end= '')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {núm} foi divisivel {cont} vezes')
if cont == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')'''
#Ex 053
#DETECTOR DE PALINDROMO
'''frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('TEMOS UM PALÍDROMO')
else:
    print('A frase digitada não é um palíndromo')'''


#Ex 054
#Grupo da Maioridade

'''from datetime import date
atual = date.today().year
totmaior = totmenor = 0
for pess in range(1, 8):
    nasc = int(input(f'Em que ano a {pess}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        print('Essa pessoa é maior')
        totmaior += 1
    else:
        print('Essa pessoa é menor')
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'E também tivemos {totmenor} pessoas menores de idade')'''
#Ex 055
#Maior e menor da sequência
'''maior = menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}kg')
print(f'O menor peso lido foi de {menor}kg')'''


#Ex 056
#Analisador completo
s_ida = 0
m_ida = 0
m_ida_h = 0
nome_velho = ''
tot_m_20 = 0
for c in range(1,5):
    print('='*15, end=' ')
    print(f'{c}ª PESSO', end=' ')
    print('='*15)
    Nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    s_ida += idade
    if p == 1 and sexo in 'Mm':
        m_ida_h = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > m_ida_h:
        m_ida_h = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        tot_m_20 +=1
m_ida = s_ida / 4
print(f'A média de idade do grupo é de {m_ida} anos')
print(f'O homem mais velhor tem {m_ida_h} anos e se chama {nome_velho}')
print(f'Ao todo são {tot_m_20} mulheres com menos de 20 anos')
