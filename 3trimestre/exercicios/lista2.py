#exercicio1
#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

# num = int(input('Digite um numero:'))
#
# if num > 0 :
#     print('Positivo')
# elif num == 0:
#     print('Neutro')
# else:
#     print('Negativo')

#exercicio2
#Faça um Programa que peça dois números e imprima o maior deles.
# num1 = int(input('Digite o primeiro numero: '))
# num2 = int(input('Digite o segundo numero: '))
#
# if num1 > num2 :
#     print('Primerio numero maior com valor: {}'.format(num1))
# elif num2 == num1:
#     print('Os numeros são iguais')
# else:
#     print('Segundo numero maior com valor: {}'.format(num2))

#exercicio7
#Crie um programa que peça uma nota de trabalho e uma de prova (as duas de 0 a 100).
#Se a média aritmética das notas for maior ou igual a 60, escreva “Aprovado”, se não, “Reprovado”.

# nota = int(input('Digite a nota do trabalho: '))
#
# if nota >= 60:
#     print('Aprovado')
# else:
#     print('Reprovado')

#exercicio10
#Construa um programa que mostre menu exatamente como o exemplo abaixo e implemente as funções necessárias:
#== Menu de Opções ==
#    1. Somar 2 números
#    2. Potência de um número
#    3. Raiz de grau N
#== Opção escolhida:
def somar():
    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))
    print('Resultado é: {}'.format(num1+num2))

def potencia():
    num = int(input('Digite o numero: '))
    potencia = int(input('Digite a pontencia: '))
    print('Resultado é: {}'.format(num ** potencia))

def raiz():
    num = int(input('Numero para achar raiz quadrada: '))
    grau = int(input('Numero para o grau da raiz: '))
    print('Resultado é: {}'.format(num ** (1/grau)))

while True :
    print('== Menu de Opções ==')
    print('  1. Somar 2 números')
    print('  2. Potência de um número')
    print('  3. Raiz de grau N ')
    print('  Qualquer tecla pra Sair')

opcao = int(input("Opção escolhida"))
if opcao == 1:
    somar()
elif opcao == 2:
    potencia()
elif opcao == 3:
    raiz()
else:
    False
