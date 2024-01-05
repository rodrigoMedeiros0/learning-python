#Trocar valores entre duas variaveis

var1 = 12
var2 = 31

var2, var1 = var1, var2

print(f'Var1: {var1}')
print(f'Var2: {var2}')

#Operador Condicional Ternário

menor = var1 if var1 < var2 else var2
print(f'Menor valor: {menor}')

#Generators

valores = [1,2,3,4,5,6,7,8,9]
quadrados = (item**2 for item in valores)
print(quadrados)
for valor in quadrados:
    print(valor)


#Função Enumerate() - iterar sobre elementos e retornar os elementos e seus indices de forma separada ou em conjunto

bebidas = ['Chá', 'Suco', 'Água', 'Suco', 'Refrigerante']
for i, item in enumerate(bebidas):
    print(f'Índice: {i}, Item: {item}')

temperaturas = [-1,10,5,-3,8,4,-2,-5,-7]
total = 0
for i,t in enumerate(temperaturas):
    if t < 0:
        total += 1
        print(f'A temperatura no índice {i} é negativa, com {t}°C.')

print(f'\n{total} ocorrências de números negativos')

#Gerenciamento de contexto com with

try:
    a = open('frutas.dat','r', encoding='utf-8')
    print(a.read())
except IOError:
    print('Não foi possível abrir o arquivo')
else:
    a.close()

with open('frutas.dat','r', encoding='utf-8') as a:
    for linha in a:
        print(linha, end='')