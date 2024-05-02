# importation module pour phase de test
from random import randint
import time
import matplotlib.pyplot as plt

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

t = [randint(0,100) for x in range(10000)]

depart = time.perf_counter()
print(quick_sort_for(t))
fin = time.perf_counter()

resultat = (fin - depart) * 1000

print(resultat)

########################@

# Données du tableau associé à la boucle for
taille_liste = [100, 1000, 10000, 100000]
temps_execution = [0.5, 8.2, 123.5, 1629.5]  # Temps d'exécution en millisecondes

# Tracer la courbe
plt.plot(taille_liste, temps_execution, marker='o', linestyle='-')

# Ajouter des étiquettes et un titre
plt.xlabel('Taille de la liste')
plt.ylabel('Temps d\'exécution (ms)')
plt.title('Temps d\'exécution en fonction de la taille de la liste (Boucle for)')

# Afficher la grille
plt.grid(True)

# Sauvegarder le graphique dans le dossier du code avec le nom "courbe_boucle_for.png"
plt.savefig('courbe_boucle_for.png')

# Afficher le graphique
plt.show()