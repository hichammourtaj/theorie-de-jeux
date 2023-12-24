def dilemme_prisonnier_n_joueurs(joueurs):
    choix_joueurs = [input(f"{joueur}, choisissez C pour coopérer ou D pour trahir : ") for joueur in joueurs]

    if all(choix == 'C' for choix in choix_joueurs):
        print("Tous les joueurs coopèrent. Chacun reçoit une récompense de 3 points.")
    elif all(choix == 'C' for choix in choix_joueurs[:-1]) and choix_joueurs[-1] == 'D':
        coop_joueurs = ', '.join(joueurs[:-1])
        print(f"{coop_joueurs} coopèrent, mais {joueurs[-1]} trahit. {coop_joueurs} reçoivent une récompense de 0 point, {joueurs[-1]} reçoit 5 points.")
    # Ajoutez les autres combinaisons de choix ici...

# Exemple avec trois joueurs
nombre_joueurs = int(input("Nombre de joueurs : "))
noms_joueurs = [input(f"Nom du joueur {i+1} : ") for i in range(nombre_joueurs)]

dilemme_prisonnier_n_joueurs(noms_joueurs)
'''Code pour n joueurs:

Chaque joueur effectue une opération d'entrée (input) une fois.
Le programme effectue des comparaisons pour déterminer la récompense en fonction des choix des joueurs.
La complexité est donc de l'ordre de O(n), où n est le nombre de joueurs.'''