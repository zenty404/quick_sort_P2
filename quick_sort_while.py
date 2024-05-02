# importation module pour phase de test
from random import randint
import time
import matplotlib.pyplot as plt

# fonction d'implementation de l'aglorithme de tri rapide (dit quicksort) avec une boucle while

def quick_sort_while(tab:list):
    '''Tri rapide en utilisant des boucles while.
    
    Argument :
        arr (list): La liste à trier.
        
    Return :
        list: La liste triée.
    '''
    # Si la liste est vide ou ne contient qu'un seul élément, elle est déjà triée
    if len(tab) <= 1:
        return tab
    else:
        # Choix du pivot comme premier élément de la liste
        pivot = tab[0]
        # Initialisation des listes pour stocker les éléments inférieurs et supérieurs au pivot
        moins_que_pivot, plus_que_pivot = [], []
        # Indice pour parcourir la liste
        i = 1
        # Parcours de la liste à partir du deuxième élément
        while i < len(tab):
            # Si l'élément est inférieur ou égal au pivot, il est ajouté à la liste des éléments inférieurs au pivot
            if tab[i] <= pivot:
                moins_que_pivot.append(tab[i])
            # Sinon, l'élément est ajouté à la liste des éléments supérieurs au pivot
            else:
                plus_que_pivot.append(tab[i])
            # Passage à l'élément suivant
            i += 1
        # Récursivement trier les sous-listes inférieures et supérieures au pivot, puis les concaténer
        return quick_sort_while(moins_que_pivot) + [pivot] + quick_sort_while(plus_que_pivot)

# phase de test pour 100 entier aleatoire de 0 à 100

t = [randint(0,100) for x in range(500)]
depart = time.perf_counter()
print(quick_sort_while(t))
fin = time.perf_counter()

resultat = (fin - depart) * 1000

print(resultat)

#################################

# Données du tableau associé à la boucle for
taille_liste = [100, 1000, 10000, 100000]
temps_execution = [0.6, 7.5, 105.4, 1409.2]  # Temps d'exécution en millisecondes

# Tracer la courbe
plt.plot(taille_liste, temps_execution, marker='o', linestyle='-')

# Ajouter des étiquettes et un titre
plt.xlabel('Taille de la liste')
plt.ylabel('Temps d\'exécution (ms)')
plt.title('Temps d\'exécution en fonction de la taille de la liste (Boucle while)')

# Afficher la grille
plt.grid(True)

# Sauvegarder le graphique dans le dossier du code avec le nom "courbe_boucle_for.png"
plt.savefig('courbe_boucle_while.png')

# Afficher le graphique
plt.show()