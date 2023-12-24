def dilemme_prisonnier_3_joueurs(joueur1, joueur2, joueur3):
    choix_joueur1 = input(f"{joueur1}, choisissez C pour coopérer ou D pour trahir : ")
    choix_joueur2 = input(f"{joueur2}, choisissez C pour coopérer ou D pour trahir : ")
    choix_joueur3 = input(f"{joueur3}, choisissez C pour coopérer ou D pour trahir : ")

    if choix_joueur1 == 'C' and choix_joueur2 == 'C' and choix_joueur3 == 'C':
        print("Les trois joueurs coopèrent. Chacun reçoit une récompense de 3 points.")
    elif choix_joueur1 == 'C' and choix_joueur2 == 'C' and choix_joueur3 == 'D':
        print(f"{joueur1} et {joueur2} coopèrent, mais {joueur3} trahit. {joueur1} et {joueur2} reçoivent une récompense de 0 point, {joueur3} reçoit 5 points.")
    # Ajoutez les autres combinaisons de choix ici...

# Exemple avec trois joueurs
joueur1 = input("Nom du premier joueur : ")
joueur2 = input("Nom du deuxième joueur : ")
joueur3 = input("Nom du troisième joueur : ")

dilemme_prisonnier_3_joueurs(joueur1, joueur2, joueur3)
'''Code pour 3 joueurs:

Chaque joueur effectue une opération d'entrée (input) une fois.
Le programme effectue des comparaisons pour déterminer la récompense en fonction des choix des joueurs.
La complexité est donc de l'ordre de  O(n), où n=3 dans ce cas'''