"""
6. Faça um programa que imprima na tela
 os números de 1 a 20, um abaixo do outro. 
 Depois modifique o programa para que ele mostre 
 os números um ao lado do outro.
 """

# um abaixo do outro
contador = 1
while contador <= 20:
	print(contador)
	contador += 1

# um ao lado do outro
contador = 1
while contador <= 20:
	# um parametro no final e dentro da função print
	# faz com que se mude o comportamento 
	# end= ', ' faz com que no lugar de pular linha,
	# apenas se insira uma virgula e continue na mesma
	# linha
	print(contador, end=', ')
	contador += 1