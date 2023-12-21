# lista = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# for item in lista:
#     print(item)

# palavra = 'Curitiba'
# for letra in palavra:
#     print(letra)

# for numero in range(1,11):
#     print(numero)

# nome = input('Digite seu nome: ')
# for x in range(10):
#     print(f' {x+1} {nome}')

#range('valor_inicial, valor_final, incremento)
# for x in range(2, 20, 2):
#     print(x)

pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Safira', 'Diamante', 'Turmalina')

for pedra in pedras: 
    if (pedra == 'Esmeralda'):
        print(F'Achei a pedra {pedra}!!')
        break
    print(pedra)