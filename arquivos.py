#Manipulação de arquivos de texto.

# print(f'\nMétodo de read(): \n')
# print(manipulador.readline())
# print(manipulador.readline())

# print(f'\nMétodo readlines(): \n')
# print(manipulador.readlines())

# text = input('Qual termo deseja procurar no arquivo? ')

# try:
#     manipulador = open('arquivo.txt', 'r', encoding='utf-8')

#     for linha in manipulador:
#         linha = linha.rstrip()
#         if text in linha:
#             print(f'A string foi encontrada!')
#             print(linha)
#         else:
#             print('String não encontrada!')
        
# except IOError:
#     print(f'Não foi possível abrir o arquivo.')
# else:
#     manipulador.close()

#Escrever em arquivo de testo 

try:
    manipulador = open('arquivo.txt', 'w', encoding='utf-8')

    manipulador.write('Treinamento de Python.\n')
    manipulador.write('Alterando dentro do texto com Python.')
except IOError:
    print(f'Não foi possível abrir o arquivo.')
else:
    manipulador.close()
