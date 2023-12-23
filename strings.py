nome = 'Rodrigo'
letra = nome[0]
print(letra)
print(len(nome))

frase = 'Fluminense perdeu para o Manchester City'
# split - separa as palavras dentro de uma lista
palavras = frase.split()
print(type(palavras)) 
#fatiamento
print(frase[0:3])

email = input('Digite seu endereço de email: ')
arroba = email.find('@')
print(arroba)
usuario = email[0:arroba]
dominio = email[arroba+ 1:]
print('Usuario: ' + usuario)
print('Dominio: ' + dominio)

produto = 'Hoje fui no mercado e comprei batata, arroz, feijão e suco'
print('suco' in produto)
print('a' in produto)
pos = produto.find('banana')
print(pos)

frase_minuscula = 'a galáxia está em festa!'
frase_maiuscula = frase_minuscula.upper()
print(frase_maiuscula.lower())
print(frase_maiuscula.capitalize())
print(frase_maiuscula.title())

suplemento = 'cloreto de magnésio'
n_suplemento = suplemento.replace('magnésio', 'zinco')
print(suplemento)
print(n_suplemento)

#removendo espaço em branco
frase_errada = '           A rato roeu a roupa do rei de Roma        '
print(frase_errada.lstrip())
print(frase_errada.rstrip())
print(frase_errada.strip())

#alinhando string
fruta = 'Abacate'
print(fruta)
print(fruta.rjust(20))
print(fruta.center(20))
print(fruta.ljust(20))
print(fruta.center(20, '-'))
print(fruta.startswith('A'))
print(fruta.endswith('o'))

#Docstring
"""
Docstring é uma éspecie de documentação que podemos inserir dentro de um módulo, 
função ou classe no Python, entre outros locais.Respeita deslocamento de texto e 
é multilinhas..
"""