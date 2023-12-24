def est_dominee(strategie, matrice):
    a, b = strategie
    for autre_strategie in matrice:
        autre_a, autre_b = autre_strategie
        if autre_a >= a and autre_b >= b and (autre_a > a or autre_b > b):
            return True
    return False

def elimination_strategies_dominees(matrice):
    strategies_dominees = []

    for i, strategie in enumerate(matrice):
        if strategie not in strategies_dominees and est_dominee(strategie, matrice):
            strategies_dominees.append(strategie)

    for strategie_dominee in strategies_dominees:
        matrice.remove(strategie_dominee)

    return matrice

# Matrice de stratégies donnée
matrice_strategies = [
    [(3, 1), (8, 0), (2, 6)],
    [(4, 3), (2, 2), (3, 0)],
    [(3, 2), (3, 1), (4, 1)]
]

# Stratégie dominante souhaitée
strategie_dominante_souhaitee = (4, 3)

# Convertir la matrice en une liste de paires
matrice_strategies = [tuple(element) for sous_liste in matrice_strategies for element in sous_liste]

# Vérifier si la stratégie dominante souhaitée est déjà dominante
if strategie_dominante_souhaitee in matrice_strategies:
    print(f"La stratégie dominante est déjà : {strategie_dominante_souhaitee}")
else:
    # Élimination des stratégies dominées
    matrice_strategies_apres_elimination = elimination_strategies_dominees(matrice_strategies)

    # Vérification de la présence de la stratégie dominante
    if len(matrice_strategies_apres_elimination) == 1:
        strategie_dominante = matrice_strategies_apres_elimination[0]
        print(f"La stratégie dominante est : {strategie_dominante}")
    else:
        print("Il n'y a pas de stratégie dominante après élimination des stratégies dominées.")

'''Conversion de la matrice en une liste de paires :
La conversion nécessite de parcourir chaque élément de la matrice une fois, donc la complexité est O(m×n).
Vérification initiale de la présence de la stratégie dominante souhaitée :

Cette vérification a une complexité constante O(1), car elle ne dépend pas de la taille de la matrice.
Élimination des stratégies dominées :

La fonction elimination_strategies_dominees effectue une itération sur chaque stratégie de la matrice pour vérifier si elle est dominée. 
Dans le pire cas, elle effectuera 
O(m×n2) opérations, car pour chaque stratégie, elle doit comparer avec chaque autre stratégie.
La suppression des stratégies dominées de la matrice a une complexité de O(m×n) dans le pire cas, car chaque suppression prend du temps linéaire.
Ainsi, la complexité totale du programme est dominée par la phase d'élimination des stratégies dominées, soit O(m×n2). 
Cependant, cette analyse suppose le pire scénario où chaque stratégie doit être comparée avec chaque autre stratégie. 
Dans des cas spécifiques où certaines stratégies sont rapidement éliminées, la complexité pratique peut être inférieure.'''