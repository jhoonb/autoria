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


def _merge(vetor_esq, vetor_dir):
    """
    merge
    fonte: adaptado de https://wiki.python.org.br/MergeSort
    Recebe dois vetores e intercala os dois vetores produzindo o vetor crescente
    parametro:(list) vetor_esq, vetor_dir
    retorno: (list) vetor_final
    """
    vetor_final = []
    # print('\nentrou: {} - {}'.format(vetor_esq, vetor_dir)) #teste de mesa
    while vetor_esq or vetor_dir:
        if len(vetor_esq) and len(vetor_dir):
            if vetor_esq[0] < vetor_dir[0]:
                vetor_final.append(vetor_esq.pop(0))
            else:
                vetor_final.append(vetor_dir.pop(0))

        if not len(vetor_esq):
            if len(vetor_dir):
                vetor_final.append(vetor_dir.pop(0))

        if not len(vetor_dir):
            if len(vetor_esq):
                vetor_final.append(vetor_esq.pop(0))
    #print("\n\t: saiu merge: {}".format(vetor_final)) # teste de mesa
    return vetor_final


def merge_sort(vetor):
    '''
    merge_sort
    recursivo
    fonte: adaptado de https://wiki.python.org.br/MergeSort 
    '''
    if len(vetor) > 1:
        meio = len(vetor) // 2
        return _merge(merge_sort(vetor[:meio]), merge_sort(vetor[meio:]))
    return vetor


def quick_sort(vetor):
    pass