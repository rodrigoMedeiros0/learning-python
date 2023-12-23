#Dicionário - guarda dados em chave e valor

elemento = {
    'Z': 3,
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534,
}

print(f'Elemento: {elemento['nome']}')
print(f'Densidade: {elemento['nome']}')
print(f'O dicionário possui: {len(elemento)} elementos.')

#Atualizar uma entrada
elemento['grupo'] = 'Alcalinos'
print(elemento)

#Adicionar uma entrada
elemento['periodo'] = 1
print(elemento)

#Excluir itens
# del elemento['periodo']
# print(elemento)

# elemento.clear()
# print(elemento)

# del elemento
# print(elemento)

#cria tuplas para cada chave
# print(elemento.items())
# for i in elemento.items():
#     print(i)

#cria uma lista com as chaves chave
print(elemento.keys())
for i in elemento.keys():
     print(i)

#cria uma lista com os valores de cada chave
print(elemento.values())
for i in elemento.values():
     print(i)
#iterando sobre as chaves e valores juntos
for i,j in elemento.items():
     print(f'{i}: {j}')