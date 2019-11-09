"""
ordenacao
2019 - Jhonathan P. Banczek
Escola Padre Constantino de Monte
"""


def bubble_sort(vetor):
    '''
    bubble_sort -- pior caso O(n^2) -- melhor caso O(n)
    wiki: https://pt.wikipedia.org/wiki/Bubble_sort
    parametro(list): um vetor 
    retorno (list): o vetor ordenado 
    '''
    for i in vetor:
        indice = 0
        while indice < len(vetor)-1:
            if vetor[indice] > vetor[indice+1]:
                vetor[indice], vetor[indice+1] = vetor[indice+1], vetor[indice] #swap
            indice += 1
    return vetor


def bubble_sort2(vetor):
    '''
    bubble sort com variável -- pior caso O(n^2) -- melhor caso O(n)
    pra checar se vetor está ordenado

    '''
    trocado = True
    while trocado:
        trocado = False
        indice = 0
        while indice < len(vetor)-1:
            if vetor[indice] > vetor[indice + 1]:
                aux = vetor[indice] # swap usando variavel auxiliar
                vetor[indice] = vetor[indice + 1]
                vetor[indice + 1] = aux
                trocado = True
            indice += 1
    return vetor


def insertion_sort(vetor):
    '''
    insertion_sort -- pior caso O(n^2) -- melhor caso O(n)
    wiki: https://pt.wikipedia.org/wiki/Insertion_sort
    parametro(list): um vetor 
    retorno (list): o vetor ordenado 
    '''
    indice = 1
    while indice < len(vetor):
        chave = vetor[indice]
        k = indice
        while k > 0 and chave < vetor[k - 1]:
            vetor[k] = vetor[k - 1]
            k -= 1
        vetor[k] = chave
        indice += 1
    return vetor

def selection_sort(vetor):
    '''
    selection_sort -- pior caso O(n^2) -- melhor caso O(n^2)
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
    merge_sort -- pior caso: O(n log n) -- melhor caso O(n log n)
    recursivo
    fonte: adaptado de https://wiki.python.org.br/MergeSort 
    '''
    if len(vetor) > 1:
        meio = len(vetor) // 2
        return _merge(merge_sort(vetor[:meio]), merge_sort(vetor[meio:]))
    return vetor


def quick_sort(vetor):
    '''
    quick_sort -- pior caso O(n^2) -- melhor caso O(n log n)
    fonte: https://www.dcc.fc.up.pt/~pbv/aulas/progimp/teoricas/teorica18.html
    parametro(list): um vetor 
    retorno (list): o vetor ordenado
    '''
    if len(vetor) <= 1: return vetor
    
    pivo = vetor[0]

    menor = []
    igual = []
    maior = []
    
    for i in vetor: 
        if i < pivo: menor.append(i)
    for i in vetor: 
        if i == pivo: igual.append(i)
    for i in vetor: 
        if i > pivo: maior.append(i)

    return quick_sort(menor) + igual + quick_sort(maior)


def quick_sort2(vetor):
    '''
    quick_sort -- pior caso O(n^2) -- melhor caso O(n log n)
    fonte: https://www.dcc.fc.up.pt/~pbv/aulas/progimp/teoricas/teorica18.html
    parametro(list): um vetor 
    retorno (list): o vetor ordenado
    Usando compreensão de listas - list comprehension
    '''

    if len(vetor) <= 1: return vetor

    pivo = vetor[0]

    menor = [i for i in vetor if i < pivo]
    igual = [i for i in vetor if i == pivo]
    maior = [i for i in vetor if i > pivo]

    return quick_sort2(menor) + igual + quick_sort2(maior)