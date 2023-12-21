# num = 1
# while (num <= 10):
#     print(num)
#     num += 1

nome = None

while True: 
    print('Digite seu nome ou aperte "X" para sair')
    nome = input()
    if (nome == 'x' or nome == 'X'):
        break
    print(f'Bem vindo, {nome}')
print('Finalizando programa...')
