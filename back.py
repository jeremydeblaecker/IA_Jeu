import points_adjacent
import copy

def backened(depart, obstacles, destination):
    def distance_min(dist, sp_set):                     # chosi un sommet parmis ceux adjacent au parent
        min = 10**10
        global min_index
        for points in range(400):                            # le point adjacent minimum est choisi
            if sp_set[points] == False and dist[points]<=min:
                min = dist[points]
                min_index = points
        return min_index

    graph, taille = copy.deepcopy(points_adjacent.return_matrix())
    parent = [-2 for i in range(400)]                   # chaque sommet garde son parent en memoire

    for value in obstacles:                             # obtient chaque valeur d'obstacle de la liste
        for z in range(taille):                           # rompt la connexion entre les obstacles et le reste du jeu
            graph[z][value] = 0

    dist = [10**10 for i in range(taille)]
    sp_set = [False for i in range(taille)]               # indique si il à deja été selectionne ou passe dessus dans le chemin
    dist[depart] = 0
    parent[depart] = -1

    for i in range(taille-1):
        u = distance_min(dist, sp_set)                  # return le sommet adjacent le plus proche
        sp_set[u] = True
                                                        # trouve tous les sommets adjacents à celui selectionne
        for points in range(taille):
            if sp_set[points] is False and graph[u][points] != 0 and dist[u] != 10**10 and dist[u] + graph[u][points] < dist[points]:
                dist[points] = dist[u] + graph[u][points]
                parent[points] = u


    def ancetre(dest):
        list1 = []
        stop = dest
        while parent[stop] != -1:               # recherche de l'ancetre du sommet de destination
            list1.append(parent[stop])
            stop = parent[stop]

        return list1

    destination_parent = ancetre(destination)
    return destination_parent
