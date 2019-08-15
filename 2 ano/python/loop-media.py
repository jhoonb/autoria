contagem_aluno = 1 # contador para quantidade de alunos
max_nota = int(input('insira quantidade de notas: ')) # maximo de notas
max_alunos = int(input('insira quantidade de alunos: ')) # maximo de alunos

media_da_sala = 0 # variavel para somar a media da sala

#primeiro loop (externo) loop para cada aluno: repita
while contagem_aluno <= max_alunos:
	print("= aluno: ", contagem_aluno)

	media = 0
	contagem_nota = 1
	# segundo loop (interno) loop para cada nota: repita
	while contagem_nota <= max_nota:
		nota = float(input("nota: ")) #recebe a nota e converte pra float
		media += nota # media é igual a media mais a nota
		contagem_nota += 1 # contagem + 1 / incrementa
	# fora do loop interno
	contagem_aluno += 1 # incrementa 
	media = media/max_nota # media da sala
	print("a media é: ", media)
	media_da_sala += media # soma média_da_sala com media

# fora do loop externo
print("media da sala: ", (media_da_sala/max_alunos))




