numeros = [1,4,7,9,10,12,21]

#usando map
# quadrados = list(map(lambda x: x ** 2, numeros))
# print(quadrados)

# Compreensão de Lista (list comprehension) é uma maneira elegante e concisa de criar e executar tarefas sobre listas em Python. 
quadrados = [num ** 2 for num in numeros]
print(quadrados)

#outro exemplo - criando lista com numeros pares
pares = [num for num in range(15) if num % 2 == 0]
print(pares)

#exemplo com texto
frase = 'Parabéns pelo nascimento do seu filho!'
vogais = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']

lista_vogais = [v for v in frase if v in vogais]
print(f'A frase possui {len(lista_vogais)} vogais')
print(lista_vogais)

#distributiva
distributiva = [k * m for k in [2,3,5] for m in [10,20,30]]
print(distributiva)