# exercicio3
#Faça um Programa que peça dois números e imprima a soma deles.

num1=int(input('Digite o primeiro numero: '))
num2=int(input('Digite o segundo numero: '))
soma=num1 + num2
print('Resultado da soma é {}'.format(soma))

#exercicio10
#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.

f = int(input('Digite o graus em Farenheit:'))
c = (5 * (f -32))/9
print('Graus em Celsius é {}'.format(c))

#exercicio14
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 7.5% para o
#Imposto de Renda, 8% para o INSS e 1% para o sindicato. Faça um programa que nos dê:
# salário bruto.
# quanto pagou de imposto de renda (calcule sobre o salário bruto).
# quanto pagou ao INSS (calcule sobre o salário bruto).
# quanto pagou ao sindicato (calcule sobre o salário bruto).
# o salário líquido (o que sobrou após os descontos).
# + Salário Bruto: R$
# - IR (7.5%): R$
# - INSS (8%): R$
# - Sindicato (1%): R$
# = Salário Líquido: R$

valor = int(input('Ganha quanto por hora? :'))
horas = int(input('Quantas horas trabalha por mês:'))
salario = valor * horas
print('Valor do Salario sem descontos: {}'.format(salario))
print('Valor do salario com desconto do IR: {}'.format(salario - (salario*0.075)))
print('Valor do salario com desconto do INSS: {}'.format(salario - (salario*0.08)))
print('Valor do salario com desconto do Sindicato: {}'.format(salario - (salario*0.01)))
print('Vador do salario com descontos: {}'.format(salario - ((salario*0.075) + (salario*0.08) + (salario*0.01))))
