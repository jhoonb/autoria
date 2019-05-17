"""
1. Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido. 
"""
# loop
while True:
	nota = input("informe a nota: ") # recebe dado via teclado
	nota = float(nota) # conversão
	if nota >= 0 and nota <= 10:
		break
	else:
		print('inválido. Nota tem que ser entre 0 e 10')

#fim

