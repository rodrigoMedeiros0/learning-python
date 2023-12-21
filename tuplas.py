#São imutáveis, ou seja, constantes (não da para alterar o valor depois de criado)

tupla = (4,3,6,8,8)
print(tupla)

t1 =(1,2,3,4)
t2 = (8,9,10,11, 1, 1)
r = t1 + t2
# print(r.count(1)) quantas vezes o 1 se repete
# print(r[:3]) - slice 
# print(99 in r)
# print(sum(t1)) soma dos valores
# print(min(t1)) menor valor
# print(max(t1)) maior valor

#operacoes nao disponiveis nas tuplas: .sort(), .append(), .reverse(), .pop()

#iterando sobre as tuplas
for i in r: 
    print(i)

#criado lista a partir de uma tupla
lista1 = list(r)
lista1[0] = 99
print(lista1)

#criando uma tupla a partir de uma lista
lista = [1,2,36,45]
tupla = tuple(lista)
print(tupla)

#ordenando tupla
print(sorted(r))



