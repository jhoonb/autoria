"""
Exercício 4
Faça um Programa que peça as 4 notas bimestrais
e mostre a média.
"""

nota_1 = input("Informe a 1a nota bimestral: ")
nota_2 = input("Informe a 2a nota bimestral: ")
nota_3 = input("Informe a 3a nota bimestral: ")
nota_4 = input("Informe a 4a nota bimestral: ")

# converte para float
nota_1 = float(nota_1)
nota_2 = float(nota_2)
nota_3 = float(nota_3)
nota_4 = float(nota_4)

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

# imprime a média
print("A média é: ", media)