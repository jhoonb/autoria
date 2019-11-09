"""
PROBLEMA 1
Se listamos todos os números naturais menores que 10 que
são múltiplos de 3 ou 5, nós teremos: 3, 5, 6 e 9.
A soma desses múltiplos será 23:
Ache a soma de todos os múltiplos de 3 ou
5 menores que 100."""

def solucao1():
	soma = 0
	n = 1
	while n < 100:
		if n % 3 == 0 or n % 5 == 0:
			soma += n
		n += 1

	print(soma)


# a solução 2 usa compreensão de lista
# e a função sum()
def solucao2():

	def multiplo23(x):
		return x % 3 == 0 or x % 5 == 0
	'''
	a função acima é o mesmo que 
	multiplo23 = lambda x: x % 3 == 0 or x % 5 == 0
	usando função lambda (anonima)
	'''
	soma = sum([n for n in range(1,100) if multiplo23(n)])
	print(soma)


solucao1()
solucao2()



