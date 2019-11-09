'''
Jhonathan P. Banczek
2019 - Escola Padre Constantino de Monte
'''

unidade = {	
	'0': 'zero',
	'1': 'um',
	'2': 'dois',
	'3': 'três',
	'4': 'quatro',
	'5': 'cinco',
	'6': 'seis', 
	'7': 'sete',
	'8': 'oito',
	'9': 'nove'
}

dezena = {
	'10': 'dez',
	'11': 'onze',
	'12': 'doze',
	'13': 'treze',
	'14': 'catorze',
	'15': 'quinze',
	'16': 'dezesseis',
	'17': 'dezessete',
	'18': 'dezoito',
	'19': 'dezenove', 
	'20': 'vinte',
	'30': 'trinta',
	'40': 'quarenta',
	'50': 'cinquenta',
	'60': 'sessenta',
	'70': 'setenta',
	'80': 'oitenta',
	'90': 'noventa'
}

centena = {
	'100': 'cem',
	'200': 'duzentos',
	'300': 'trezentos',
	'400': 'quatrocentos',
	'500': 'quinhentos',
	'600': 'seiscentos',
	'700': 'setecentos',
	'800': 'oitocentos',
	'900': 'novecentos',
	'1000': 'mil'
}

print("Conversor de número para por extenso")
print("digite um número >= 0 ou -1 para sair. ")
while True:
	
	valor = input("digite um número: ")
	
	if valor == '-1': 
		break

	# 0 até 9
	if len(valor) == 1:
		print(unidade[valor])

	# 10 até 99
	elif len(valor) == 2:
		# se for 10, 20,30,40,50,60,70,80,90 ...
		if valor in dezena:
			print(dezena[valor])
		# se for 11, 12, ... 83, 99...
		else:
			valor_dezena = dezena[valor[0]+'0']
			print("{} e {}".format(valor_dezena, unidade[valor[-1]]))
	# 100 até 999
	elif len(valor) == 3:
		if valor in centena:
			print(centena[valor])
		else:
			print("nao implementado")

	else:
		print('nao implementado')

'''

extenso = {
	'0': 'zero',
	'1': 'um',
	'2': 'dois',
	'3': 'três',
	'4': 'quatro',
	'5': 'cinco',
	'6': 'seis', 
	'7': 'sete',
	'8': 'oito',
	'9': 'nove',
	'10': 'dez',
	'11': 'onze',
	'12': 'doze',
	'13': 'treze',
	'14': 'catorze',
	'15': 'quinze',
	'16': 'dezesseis',
	'17': 'dezessete',
	'18': 'dezoito',
	'19': 'dezenove', 
	'20': 'vinte',
	'30': 'trinta',
	'40': 'quarenta',
	'50': 'cinquenta',
	'60': 'sessenta',
	'70': 'setenta',
	'80': 'oitenta',
	'90': 'noventa',
	'100': 'cem',
	'101': 'cento', # usar este como padrão de 'cento'
	'200': 'duzentos',
	'300': 'trezentos',
	'400': 'quatrocentos',
	'500': 'quinhentos',
	'600': 'seiscentos',
	'700': 'setecentos',
	'800': 'oitocentos',
	'900': 'novecentos',
	'1000': 'mil'
}

print("Conversor de número para por extenso")
print("digite um número >= 0 ou -1 para sair. ")
while True:
	
	valor = input("digite um número: ")
	
	if valor == '-1': 
		break

	# se for valor menos que 10
	if len(valor) == 1: 
		print(extenso[valor])

	# se valor for maior igual a 10 e menor igual a 20
	elif int(valor) >= 10 and int(valor) <= 20:
		print(extenso[valor])

	# se valor for maior que 20 e que termina em 0
	elif len(valor) == 2 and valor[1] == '0':
		print(extenso[valor])

	# se valor for menor que 99	
	elif int(valor) <= 99:
		# pega o primeiro digito acrescenta um 
		# 0 para pegar a dezena por extenso, depois usa o conectivo e
		# para juntar com a unidade 
		v = "{} e {}".format(extenso[valor[0] + "0"], extenso[valor[1]])  
		print(v)
	# 100 ao 1000
	elif int(valor) >= 100 and int(valor) <= 1000:
		if valor == '100':
			print(extenso[valor])
		else:
			grandeza = '{}01'.format(valor[0]) if valor[0] == 1 else '{}00'.format(valor[0])   
			dezena =  extenso[valor[1]+"0"]
			unidade = " e " + extenso[valor[-1]] if valor[-1] != '0' else ''
			print("{} e {}{}".format(grandeza, dezena, unidade))
	else:
		print("não implementado...")

'''