"""
ordenacao
2019 - Jhonathan P. Banczek
Escola Padre Constantino de Monte
"""


def bubble_sort(vetor):
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
    pass

def selection_sort(vetor):
    pass 

def merge_sort(vetor):
    pass

def quick_sort(vetor):
    pass