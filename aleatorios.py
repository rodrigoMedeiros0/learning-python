import random

# valor = random.randint(1, 20)
# print(valor)

# print('Gerar 5 números aleatórios entre 1 e 50: \n')
# for i in range(5):
#     numero = random.randint(1, 50)
#     print(f'Numero gerado: {numero}')

# valor = random.random()
# print(f'Número gerado: {round(valor * 10, 2) }')

# valor = random.uniform(1, 100)
# print(f'Número: {round(valor, 1)}')

L = [2,3,6,66,77,45,23,14, 15, 44, 69]
# n = random.choice(L)
# print(f'Número escolhido: {n}')
# n = random.sample(L, 3)
# print(f'Números escolhidos: {n}')

#embaralhar
print(f'Lista original: {L}')
n = random.shuffle(L)
print(f'Lista embaralhada: {L}')