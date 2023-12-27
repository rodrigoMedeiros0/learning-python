#Escopo Global e Local

var_global = 'Café gelado'

def escreve_texto():
    global var_global
    var_local = 'Rodrigo Medeiros'
    var_global = 'Suco de abacaxi'
    print(f'Variável Global: {var_global}')
    print(f'Variável Local: {var_local}')

if __name__ == '__main__':
    print(f'Executar a função escreve_texto()')
    escreve_texto()

    print('Tentar acessar as variáveis diretamente')
    print(f'Variável Global: {var_global}')