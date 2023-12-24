def dilemme_prisonnier(joueur1, joueur2):
    choix_joueur1 = input(f"{joueur1}, choisissez C pour coopérer ou D pour trahir : ")
    choix_joueur2 = input(f"{joueur2}, choisissez C pour coopérer ou D pour trahir : ")

    if choix_joueur1 == 'C' and choix_joueur2 == 'C':
        print("Les deux joueurs coopèrent. Chacun reçoit une récompense de 3 points.")
    elif choix_joueur1 == 'C' and choix_joueur2 == 'D':
        print(f"{joueur1} coopère et {joueur2} trahit. {joueur1} reçoit une récompense de 0 point, {joueur2} reçoit 5 points.")
    elif choix_joueur1 == 'D' and choix_joueur2 == 'C':
        print(f"{joueur1} trahit et {joueur2} coopère. {joueur1} reçoit 5 points, {joueur2} reçoit 0 point.")
    elif choix_joueur1 == 'D' and choix_joueur2 == 'D':
        print("Les deux joueurs trahissent. Chacun reçoit une récompense de 1 point.")

# Exemple avec deux joueurs
joueur1 = input("Nom du premier joueur : " )
joueur2 = input("Nom du deuxième joueur : ")

dilemme_prisonnier(joueur1, joueur2)
'''Code pour 2 joueurs:

Chaque joueur effectue une opération d'entrée (input) une fois.
Le programme effectue des comparaisons pour déterminer la récompense en fonction des choix des joueurs.
La complexité est donc de l'ordre de O(n), où n=2
 dans ce cas.'''
