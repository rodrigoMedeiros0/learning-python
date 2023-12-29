#funcoes lambda (anônimas) 
    #sintaxe:
    #lambda argumentos: expressao

quadrado = lambda x: x**2
for i in range(1,11):
    print(quadrado(i))

f_c = lambda f: (f - 32) * 5/9
print(f_c(212))

#funcao map() - aplica uma função em cada item de uma lista de itens
    #sintaxe:
    #map(função, iterável)

# num = [1,2,3,4,5,6,7,8,9]
# dobro = list(map(lambda x: x*2, num))
# print(dobro)

palavras = ['Python','django','Javascript', 'html', 'css']
transform_string_upper = lambda x: x.upper()
upper = list(map(transform_string_upper, palavras))
print(upper)

#funcao filter - 
    #Sintaxe:
    #filter(função, sequencia)
def numeros_pares(x):
    return x % 2 == 0

numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13]

num_par = list(filter(numeros_pares, numeros))
print(num_par)
num_impar = list(filter(lambda x: x %2 != 0, numeros))
print(num_impar)


#funcao reduce() -  útil quando precisamos agregar todos os elementos de um conjunto em um único valor
    #sintaxe:
    #reduce(função, sequência, valor_inicial)

from functools import reduce

def mult(x, y):
    return x * y

numeros = [1,2,3,4,5,6]

total = reduce(mult, numeros)
print(total)

#exemplo: função cumulativa dos quadrados dos valores usando lambda
numeros = [1,2,3,4]
total = reduce(lambda x,y: x ** 2 + y ** 2, numeros)
print(total)
