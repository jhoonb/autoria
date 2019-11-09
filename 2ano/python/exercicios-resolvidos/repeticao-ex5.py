'''
5. Altere o programa anterior (repeticao-ex4.py) permitindo
ao usuário informar as populações e as 
taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação.
'''

while True:
	print("-" * 70)
	opc = input('deseja iniciar o programa: s | n: ')
	if opc == 'n':
		print('\tprograma finalizado')
		break

	# valida a entrada da pop A e B.
	while True:
		pais_a_populacao = int(input("população país A: "))
		pais_b_populacao = int(input("população país B: "))
		if pais_a_populacao >= pais_b_populacao:
			print('informe um valor maior pra populacao B')
		else:
			break
	# recebe taxa de crescimento
	pais_a_tx_crescimento = float(input("taxa de crescimento do país A: "))
	pais_b_tx_crescimento = float(input("taxa de crescimento do país B: "))

	# gera a porcentagem
	pais_a_tx_crescimento = pais_a_tx_crescimento / 100
	pais_b_tx_crescimento = pais_b_tx_crescimento / 100
	
	# variaveis pro aumento
	pais_a_aumento = 0
	pais_b_aumento = 0
	qnt_anos = 1

	print("\tcalculando ... ")
	while True:
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