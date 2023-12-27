#Funcoes

def mensagem(x,y): 
    result = x +y 
    return print(f'Resultado da soma de {x} + {y} é {result}')

mensagem(5,10)

def div (k,j):
    if j != 0:
        return k / j
    else:
        return 'Impossivel dividir por zero'
if __name__ == '__main__':
    a = int(input('Digite um número: '))
    b = int(input('Digite otruo número: '))

    r = div(a,b)
    print(f'{a} dividido por {b} é igual a {r}')

def quadrado(val):
    quadrados = []
    for x in val:
        quadrados.append(x ** 2)
    return quadrados

if __name__ == '__main__':
    valores = [2, 5, 7, 9, 12]
    resultados = quadrado(valores)
    for i in resultados:
        print(i)

def contar(num=11, caractere='+'):
    for i in range(1, num):
        print(caractere)

if __name__ == '__main__':
    # contar(num=5 ,caractere='$')
    contar(2, '@')