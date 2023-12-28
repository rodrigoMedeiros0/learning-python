from math import sqrt

class NumeroNegativoError(Exception):
    def __init__(self):
        pass

if __name__ == '__main__':
    try:
        num = int(input('Digite um numero positivo: '))
        if num < 0:
            raise NumeroNegativoError
    except NumeroNegativoError:
        print(f'Foi fornecido um numero negativo. Digite um numero positivo, por favor!')
    else:
        print(f'A raiz quadrada de {num} é {sqrt(num)}')
    finally:
        print('Fim do cálculo...')

# if __name__ == '__main__':
#     try:
#         num = int(input('Digite um numero positivo: '))
#         if num < 0:
#             raise ArithmeticError
#     except ArithmeticError:
#         print(f'Foi fornecido um numero negativo. Digite um numero positivo, por favor!')
#     else:
#         print(f'A raiz quadrada de {num} é {sqrt(num)}')
#     finally:
#         print('Fim do cálculo...')

    