# importation module pour phase de test
from random import randint
import time

# fonction d'implementation de l'aglorithme de tri rapide (dit quicksort) avec une boucle for

def quick_sort_for(tab:list):
    '''Tri rapide en utilisant des boucles for.
    
    Argument :
        tab (list): La liste à trier.
        
    Return :
        list: La liste triée.
    '''
    
    # Si la liste est vide ou ne contient qu'un seul élément, elle est déjà triée
    if len(tab) <= 1:
        return tab
    else:
        # Choix du pivot comme premier élément de la liste
        pivot = tab[0]
        # Partitionnement de la liste en deux parties : inférieure et supérieure au pivot
        moins_que_pivot = [x for x in tab[1:] if x <= pivot]
        plus_que_pivot = [x for x in tab[1:] if x > pivot]
        # Récursivement trier les sous-listes inférieures et supérieures au pivot, puis les concaténer
        return quick_sort_for(moins_que_pivot) + [pivot] + quick_sort_for(plus_que_pivot)


# phase de test pour 100 entier aleatoire de 0 à 100

t = [randint(0,100) for x in range(100)]

depart = time.perf_counter()
print(quick_sort_for(t))
fin = time.perf_counter()

resultat = (fin - depart) * 1000

print(resultat)