"""
2. Faça um programa que leia um nome de 
usuário e a sua senha e não aceite a 
senha igual ao nome do usuário, mostrando
 uma mensagem de erro e voltando a pedir as informações. 
"""

nome = input('informe seu nome: ')
while True:
	senha = input('informe a senha: ')
	if senha != nome:
		break
	print("A senha não pode ser o nome do usuário, informe outra.")
		
