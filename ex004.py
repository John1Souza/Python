n = input('Digite algo: ')

print('O tipo primitivo desse valor é: ', type(n))
print('É alfanumérico?', n.isalnum())
print('Só tem espaços?',n.isspace())
print('É decimal?', n.isdecimal())
print('É numero?', n.isnumeric())
print('É alfabético?', n.isalpha())
print('Está em maiúsculas?', n.isupper())
print('Está em minúsculas?', n.islower())
print('Está capitalizada?', n.isidentifier())