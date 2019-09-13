"""
ordenacao
2019 - Jhonathan P. Banczek
Escola Padre Constantino de Monte
"""


def bubble_sort(vetor):
    '''
    bubble_sort -- pior caso O(n^2)
    wiki: https://pt.wikipedia.org/wiki/Bubble_sort
    parametro(list): um vetor 
    retorno (list): o vetor ordenado 
    '''
    for i in vetor:
        indice = 0
        while indice <= len(vetor)-1:
            if indice == len(vetor)-1:
                break 
            if vetor[indice] > vetor[indice+1]:
                vetor[indice], vetor[indice+1] = vetor[indice+1], vetor[indice]
            indice += 1
    return vetor


def insertion_sort(vetor):
    '''
    insertion_sort -- pior caso O(n^2)
    wiki: https://pt.wikipedia.org/wiki/Insertion_sort
    parametro(list): um vetor 
    retorno (list): o vetor ordenado 
    '''
    indice = 1
    while indice < len(vetor):
        chave = vetor[indice]
        j = indice
        while (j > 0) and (vetor[j-1] > chave):
            vetor[j] = vetor[j-1]
            j -= 1
        vetor[j] = chave 
        indice += 1
    return vetor




def selection_sort(vetor):
    '''
    selection_sort -- pior caso O(n^2)
    wiki: https://pt.wikipedia.org/wiki/Selection_sort
    parametro(list): um vetor 
    retorno (list): o vetor ordenado 
    '''
    indice = 0
    while indice < len(vetor):
        menor = indice
        j = indice + 1
        while j < len(vetor):
            if vetor[j] < vetor[menor]:
                menor = j
            j += 1
        vetor[indice], vetor[menor] = vetor[menor], vetor[indice]
        indice += 1
    return vetor


def merge_sort(vetor):
    pass

def quick_sort(vetor):
    pass