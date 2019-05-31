1) Faça um Programa que leia um vetor de 5 
números inteiros e mostre-os.

2) Faça um Programa que leia um vetor de 10 
números reais e mostre-os na ordem inversa.

3) Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

4) Faça um Programa que leia um vetor de 10 caracteres, 
e diga quantas consoantes foram lidas. 
Imprima as consoantes.

5) Faça um Programa que leia 20 números inteiros 
e armazene-os num vetor. Armazene os números 
pares no vetor PAR e os números IMPARES no 
vetor impar. Imprima os três vetores.


6) Faça um programa que leia um número indeterminado de valores, 
correspondentes a notas, encerrando a entrada de dados quando 
for informado um valor igual a -1 (que não deve ser armazenado). 
Após esta entrada de dados, faça:
- Mostre a quantidade de valores que foram lidos;
- Exiba todos os valores na ordem em que foram informados, 
	um ao lado do outro;
- Exiba todos os valores na ordem inversa à que foram 
	informados, um abaixo do outro;
- Calcule e mostre a soma dos valores;
- Calcule e mostre a média dos valores;
- Calcule e mostre a quantidade de valores acima da média calculada;
- Calcule e mostre a quantidade de valores abaixo de sete;
- Encerre o programa com uma mensagem;
ajuda:
len(lista) # retorna quantidade de elementos dentro da lista
lista = []
lista.append(valor) # add o valor no final da lista
lista.reverse() # ordem reversa da lista

7) Uma empresa de pesquisas precisa tabular os resultados da seguinte
 enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

- 1- Windows Server
- 2- Unix
- 3- Linux
- 4- Netware
- 5- Mac OS
- 6- Outro

Você foi contratado para desenvolver um programa que leia
o resultado da enquete e informe ao final o resultado da mesma.
O programa deverá ler os valores até ser informado o valor 0,
que encerra a entrada dos dados. Não deverão ser aceitos valores 
além dos válidos para o programa (0 a 6). Os valores referentes 
a cada uma das opções devem ser armazenados num vetor. 
Após os dados terem sido completamente informados, o 
programa deverá calcular a percentual de cada um dos 
concorrentes e informar o vencedor da enquete. O formato
da saída foi dado pela empresa, e é o seguinte:

`
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800
`

O Sistema Operacional mais votado foi o Unix, 
com 3500 votos, correspondendo a 40% dos votos.