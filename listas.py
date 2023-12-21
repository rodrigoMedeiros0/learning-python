# listas - representa uma sequência de valores
  #sintaxe: nome_lista = [valores]

# notas = [5,7,8,6,9]
# print(notas)

n1 = [1,5,6,8]
n2 = [9,8,4,2]
valores = n1 + n2
# print(valores)
# print(type(valores))
# print(valores[-1])
valores[0] = 22
# print(valores[0:3])
# print(len(valores))  lenght
# print(sorted(valores)) deixa em ordem crescente
# print(sorted(valores, reverse=True)) deixa em ordem decrescente
# print(sum(valores)) soma os valores dentro
# print(min(valores)) mostra o menor valor
# print(max(valores)) mostra o maior valor

#metodo para insirir valor ao final da lista
valores.append(13)
# print(valores)

#metodo para retirar elemento
# valores.pop() senao falar nada, ele pega o ultimo elemento
# valores.pop(0)
# print(valores)

#metodo para inserir um valor numa posicao especifica
# valores.insert(0, 44)
# print(valores)

#metodo para verificar se existe algum valor dentro da lista
# print(44 in valores)

# planetas = ['Mercúrio', 'Vênus', 'Marte', 'Saturno', 'Terra', 'Júpiter']
# for planeta in planetas:
#     print(planeta)

bebidas = []
for count in range(5):
    print(f'Digite o {count + 1 }° nome da sua bebida favorita: ')
    valor_input = input()
    bebidas.append(valor_input) 

bebidas.sort()

print(f'\n Bebidas escolhidas: ')
for bebida in bebidas:
    print(bebida) 