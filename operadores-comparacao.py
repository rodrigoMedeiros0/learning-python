# == igual a 
# != diferente de 
# > maior que 
# < menor que 
# >= maior ou igual a 
# <= menor ou igual a  

print('Digite um numero: ')
n1 = int(input())
n2 = int(input('Digite outro numero: '))

x = n1 == n2
print('Os valores são iguais?', x, '\n')

y = n1 != n2
print('São diferentes? ' + str(y))