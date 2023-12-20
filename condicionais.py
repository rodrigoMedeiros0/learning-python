#simples, composto e encadeado

n1 = n2 = 0.0
media = 0.0

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

#Calcular a media aritmetica das notas 
media = (n1 + n2) / 2 

if (media >= 7): 
    print('Aluno aprovado!')
    print('Parabéns')
elif (media >= 5): 
    print('Aluno em recuperação!')
else: 
    print('Aluno reprovado...')

print('Sua media é {}' .format(media))