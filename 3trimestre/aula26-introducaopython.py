# Comentario em python

print("Ola Mundo :D")

'''
Comentario em bloco
'''

#variaveis não ha necessidade de tipagem assume qualquer valor/tipo

num = 10
nome = 'fabio'

#concatenação jeito simples por virgula

print('o resultado é', num, 'certo?')

print('o resultado é {}, certo?'.format(num))

print('{}, o resultado é {}, certo?'.format(nome,num))

#Operador de potencia

num = 5 ** 2 # 5 ao quadrado
num = 5 ** 3 # 5 ao cubo

# Prioridade de operadores
# ** potencia
# * multiplicação
# / divisão
# + adição
# - subtração

num = 9 ** (1/2) #raiz quadrado

if(num % 2 = 0):
    print('o numero {} é par!'.format(num))

print('fim fo if')

else:
    print('o numero {} é ímpar!'.format(num))


###############################################3333
num = int(input('Digite o numero:'))
i=0

while(i <=10):
    print('{} X {} = {}')
