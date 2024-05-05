# proramme pour tracer la courbe de compléxité de l'implementation avec 'for'

# importation
import matplotlib.pyplot as plt


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