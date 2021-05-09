import points_adjacent
import copy

def backened(depart, obstacles, destination):
    def min_distance(dist, sp_set):                     # chosi un sommet parmis ceux adjacent au parent
        min = 10**10
        global min_index
        for v in range(400):                            # le point adjacent minimum est choisi
            if sp_set[v] == False and dist[v]<=min:
                min = dist[v]
                min_index = v
        return min_index

    graph, size = copy.deepcopy(points_adjacent.return_matrix())
    parent = [-2 for i in range(400)]                   # chaque sommet garde son parent en memoire

    for value in obstacles:                             # obtient chaque valeur d'obstacle de la liste
        for z in range(size):                           # rompt la connexion entre les obstacles et le reste du jeu
            graph[z][value] = 0

    dist = [10**10 for i in range(size)]
    sp_set = [False for i in range(size)]               # indique si il à deja été selectionne ou passe dessus dans le chemin
    dist[depart] = 0
    parent[depart] = -1

    for i in range(size-1):
        u = min_distance(dist, sp_set)                  # return le sommet adjacent le plus proche
        sp_set[u] = True
                                                        # trouve tous les sommets adjacents à celui selectionne
        for v in range(size):
            if sp_set[v] is False and graph[u][v] != 0 and dist[u] != 10**10 and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
                parent[v] = u


    def ancestor(dest):
        list1 = []
        stop = dest
        while parent[stop] != -1:               # recherche de l'ancetre du sommet de destination
            list1.append(parent[stop])
            stop = parent[stop]

        return list1

    destination_parent = ancestor(destination)
    return destination_parent
