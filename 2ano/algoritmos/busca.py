"""
busca binária
2019 - Jhonathan P. Banczek
Escola Padre Constantino de Monte
"""


def busca_binaria(vetor, valor):
    '''
    busca_binaria -- O(log n)
    parametro vetor(list): uma lista ordenada
    parametro valor(int): um valor a procurar na lista
    retorno(int): o indice do valor no vetor, ou -1 se nao encontrou
    '''
    indice_baixo = 0
    indice_alto = len(vetor)-1
    while indice_baixo <= indice_alto:
        indice_meio = int((indice_alto + indice_baixo) / 2)
        valor_chute = vetor[indice_meio]
        if valor_chute > valor: 
            indice_alto = indice_meio - 1
        elif valor_chute < valor:
            indice_baixo = indice_meio + 1
        else:
            return indice_meio
    return -1


def busca_sequencial(vetor, valor):
    '''
    busca_sequencial -- O(n)
    parametro vetor(list): uma lista ordenada
    parametro valor(int): um valor a procurar na lista
    retorno(int): o indice do valor no vetor, ou -1 se nao encontrou
    '''
    indice = 0
    while indice <= len(vetor)-1:
        if vetor[indice] == valor:
            return indice
        indice += 1
    return -1 


