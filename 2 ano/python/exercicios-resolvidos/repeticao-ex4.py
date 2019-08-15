'''4. Supondo que a população de um país A seja da
ordem de 80000 habitantes
com uma taxa anual de crescimento de 3% 
e que a população de B seja 200000 habitantes
com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e
escreva o número de anos necessários para que a 
população do país A ultrapasse ou iguale 
a população do país B, mantidas as taxas de crescimento.
'''

# primeiro definimos as variáveis
pais_a_populacao = 8_000
pais_a_tx_crescimento = 0.03 # 3%
pais_a_aumento = 0

pais_b_populacao = 200_000
pais_b_tx_crescimento = 0.015 # 1.5%
pais_b_aumento = 0

qnt_anos = 1
while True:
	print('ano: ', qnt_anos)
	# calcula aumento pro país A
	pais_a_aumento = pais_a_populacao * pais_a_tx_crescimento
	pais_a_populacao += pais_a_aumento
	# calcula aumento pro país B
	pais_b_aumento = pais_b_populacao * pais_b_tx_crescimento
	pais_b_populacao += pais_b_aumento
	# verifica se país A passou ou igualou 
	# a população do país B
	if pais_a_populacao >= pais_b_populacao:
		print("\nPopulação do país A: ", pais_a_populacao)
		print("\nPopulação do País B: ", pais_b_populacao)
		print("País A passou ou igualou o País B em :", qnt_anos, " anos")
		break
	qnt_anos += 1
