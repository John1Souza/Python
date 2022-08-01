brasileirão =('Corinthians','Palmeiras', 'São Paulo', 'Internacional', 'Atlético-MG', 'Athletico-PR','Ceará','Coritiba','Fluminense', 'América-MG', 'Santos', 'Bragantino', 'Goiás', 'Atlético-GO', 'Flamengo', 'Botafogo', 'Cuiabá', 'Avaí', 'Juventude', 'Fortaleza')
print('-='*15)
#5 PRIMEIROS COLOCADOS
a = brasileirão[0:5]
print(f'Os 5 primeiros colocados do Brasileirão são {a}')
print('-='*15)
# 4 ULTIMOS COLOCADOS
b = brasileirão[-5:-1]
print(f'Os 4 ultimos colocados do Brasileirão são {b}')
print('-='*15)
# ORDEM ALFABÉTICA
print('-='*15)
c = sorted(brasileirão)
print(f'A lista com os times em ordem alfabética {c}')

# LOCALIZAÇÃO CHAPECOENSE ==> INTERNACIONAL
print('-='*15)
d = brasileirão.index('Internacional')
print(f'O time Internacional está na {d+1}ª posição ')
print('-='*15)