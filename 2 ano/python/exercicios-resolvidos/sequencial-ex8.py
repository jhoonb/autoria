"""
Exercício 8
Faça um Programa que pergunte quanto você ganha 
por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.
"""

valor_hora = input("Quanto você ganha por hora? ")
qnt_horas = input("Quantas horas trabalha no mês? ")

# converte
valor_hora = float(valor_hora)
qnt_horas = float(qnt_horas)

print("total do salario no mês R$: ", valor_hora * qnt_horas)