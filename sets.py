#set - conjuntos (coleções não ordenadas)
 #Diferença dicionario e set
    ## Dicionario adiciona chave e valor
    ## Set adiciona apenas valores, não existe valores duplicados

planeta_anao = {
    'Plutão',
    'Ceres',
    'Eris',
    'Haumea',
    'Makemake'
}

print(planeta_anao)
print(type(planeta_anao))
print(type(len(planeta_anao)))
print('Ceres' in planeta_anao)
print('Lua' in planeta_anao)

for astro in planeta_anao:
    print(astro.upper())

astros = ['Lua', 'Vênus', 'Sirius', 'Marte', 'Lua']
print(astros, end=' ')
astros_set = set(astros)
print(astros_set)


astros1 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Io'}
astros2 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Cometa de Halley'}
print(astros1 == astros2)
print(astros1 != astros2)
print(astros1 | astros2)
print(astros1.union(astros2))

#pega os elementos que existem em ambos os cojuntos
print(astros1 & astros2)
print(astros1.intersection(astros2))

#retorna os valores diferentes
print(astros1 ^ astros2)
print(astros1.symmetric_difference(astros2))

astros1.add('Urano')
astros1.add('Sol')
print(astros1)

astros1.remove('Io')
print(astros1)

#o discard nao dá erro caso ele nao ache algum valor inexiste
astros1.discard('XX')
print(astros1)

astros1.clear()
print(astros1)




