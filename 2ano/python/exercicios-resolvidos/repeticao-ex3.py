"""
3. Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

# loop para o nome
while True:
	nome = input("informe nome: ")
	if len(nome) >= 3:
		break
	print('\tNome inválido. Nome: maior que 3 caracteres')

# loop para a idade
while True:
	idade = int(input("informe a idade: "))
	if idade >= 0 and idade <= 150:
		break
	print('\tIdade inválida. Idade: entre 0 e 150')

# loop para o salario
while True:
	salario = float(input("informe salario: "))
	if salario > 0:
		break
	print('\tSalário inválido. Salário: maior que zero')

# loop para o sexo
while True:
	sexo = input("informe o sexo: ")
	if sexo == 'm' or sexo == 'f':
		break
	print('\tSexo inválido. Sexo: "f" ou "m"')

# loop para o estado civil
while True:
	estado_civil = input("informe o estado civil: ")
	if estado_civil == 's' or estado_civil == 'c':
		break
	if estado_civil == 'v' or estado_civil == 'd':
		break
	print("\tEstado civil inválido. Estado Civil: 's', 'c', 'v', 'd'")

# imprime todos os dados
print('\tNome: ', nome)
print('\tIdade: ', idade, "anos")
print('\tSalario: R$ ', salario)

if sexo == 'm':
	print('\tSexo: Masculino')
else:
	print('\tSexo: Feminino')

if estado_civil == 'c':
	print('\tEstado Civil: Casado')
elif estado_civil == 's':
	print('\tEstado Civil: Solteiro')
elif estado_civil == 'v':
	print('\tEstado Civil: Viúvo')
else:
	print('\tEstado Civil: Divorciado')


