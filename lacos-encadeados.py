# for rodada in range(1, 6):
#     print(f'\nRodada: {rodada}')
#     for cont_interno in range(5, 0, -1):
#         print(f'Valor: {cont_interno}')

# print("Fim dos laços")

import random

for A in range(1, 6):
    print(f'\nConjunto {A}')
    for B in range(5):
        num = random.randint(1, 100)
        print(f' .Valor: {num}')