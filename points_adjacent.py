def lien(i, j):
    vertical = 20
    vertical_rem = 19

    if i == j:                                                          # On vérifie si les sommets sont les mêmes
        return 0
    if i % vertical != 0 and i % vertical != vertical_rem:              # on verifie les colonnes (sauf la derniere et la premiere)
        if i+1 == j or i-1 == j or i+vertical == j or i-vertical == j:
            return 1

        else:
            return 0
    elif i % vertical == 0:                                             # si la premiere colonne
        if i+1 == j or i+vertical == j or i-vertical == j:
            return 1

        else:
            return 0
    elif i % vertical == vertical_rem:                                  # si la derniere colonne
        if i-1 == j or i+vertical == j or i-vertical == j:
            return 1

        else:
            return 0

#initialisation de la matrice adjacente
row_col_size = 20
taille = row_col_size*row_col_size
matrice_adj = [[0 for i in range(taille)] for j in range(taille)]

#On vérfie si les éléments sont adjacents ou non
for i in range(0, taille):
    for j in range(0, taille):
        resultat = lien(i, j)
        matrice_adj[i][j] = resultat

def return_matrix():
    return matrice_adj, taille