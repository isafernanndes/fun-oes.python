def contar_vogais(string):
    vogais = 'aeiouAEIOU'
    return sum(1 for char in string if char in vogais)
p= input('digite uma palavra: ')
print('n° de vogais = {}'.format(contar_vogais(p)))