from tkinter import *
import back


def Jeu():
    root = Tk()
    root.title('IA de jeu')
    root.geometry('900x900')
    count = 0  # permet d'identifier chaque boutons et leur donnees un parametre unique
    button_list = []  # stock les boutons selectionnes pendant le jeu

    # On créé deux frames
    frame_up = LabelFrame(root, text='Edition')  # On définit le nom de l'editeur
    frame_down = LabelFrame(root, text='Labyrinthe')  # On définit le nom de l'environnement de jeu
    frame_up.pack()
    frame_down.pack()

    global type_elements  # pour différencier le départ, la fin et les obstacles
    type_elements = 0

    global depart  # Point de départ
    depart = 0

    global liste_obstacles  # stock les obstacles quand type_elements is 2
    liste_obstacles = []

    global destination  #variable destination final
    destination = 1000

    def button_mode(mode):  # on definit : depart/obstacles/destination
        global type_elements
        type_elements = mode
        print(type_elements)

    def Niveau_1():
        obstacles_pregenere = [40, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 41, 61,
                                      81, 101, 121, 141, 161, 181, 182, 201, 221, 241, 261, 281, 301, 321, 341, 361,
                                      362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377,
                                      378, 379, 339, 338, 318, 298, 278, 258, 238, 239, 219, 199, 179, 159, 139, 119,
                                      99, 79, 59, 39, 43, 63, 83, 103, 45, 65, 85, 123, 105, 143, 144, 145, 146, 186,
                                      185, 184, 183, 122, 106, 108, 88, 68, 48, 26, 90, 110, 49, 50, 51, 52, 53, 91, 92,
                                      93, 95, 115, 135, 155, 175, 195, 215, 235, 255, 172, 212, 152, 151, 150, 149, 148,
                                      187, 189, 188, 169, 230, 231, 232, 229, 228, 227, 54, 55, 56, 77, 57, 117, 97,
                                      118, 156, 176, 196, 216, 236, 178, 173, 174, 225, 224, 223, 243, 263, 283, 323,
                                      324, 325, 326, 327, 328, 329, 309, 289, 269, 249, 265, 285, 286, 287, 267, 297,
                                      296, 295, 294, 293, 292, 252, 253, 291, 330, 331, 332, 333, 334, 335, 336, 337,
                                      264, 288]
        global liste_obstacles
        liste_obstacles = obstacles_pregenere
        for every in obstacles_pregenere:
            button_list[every].config(bg='#484848')

    level_button = Button(frame_up, text='Niveau 1', command=Niveau_1)
    level_button.grid(row=0, column=1, padx=10, pady=5)

    def Niveau_2():
        obstacles_pregenere = [2,3,4,5,6,7,16,22,27,35,41,53,69,71,72,73,76,77,78,83,
                               84,86,90,93,98,102,113,118,125,126,128,144,153,157,174,
                               184,188,189,190,191,194,204,224,234,241,248,249,254,261,
                               264,266,267,274,275,276,277,278,281,284,289,290,301,304,307,
                               308,309,311,314,321,322,324,325,336,337,342,349,356,357,
                               362,364,365,367,369,372,377,383,386,399]
        global liste_obstacles
        liste_obstacles = obstacles_pregenere
        for every in obstacles_pregenere:
            button_list[every].config(bg='#484848')

    level_button = Button(frame_up, text='Niveau 2', command=Niveau_2)
    level_button.grid(row=0, column=2, padx=10, pady=5)

    def boutous_cliques(but_num):  # Bouttons cliques dans le labyrinthe
        global type_elements
        if type_elements == 1:  # point de depart type_elements = 1
            button_list[but_num].config(bg='#FFFF00') #On affiche le point de depart en jaune
            global depart
            depart = but_num
            start_button['state'] = DISABLED
            type_elements = 0
        if type_elements == 2:  # obstacles type_elements = 2
            button_list[but_num].config(bg='#484848') #On affiche les murs en gris
            global liste_obstacles
            liste_obstacles.append(but_num)
        if type_elements == 3:  # destination type_elements = 3
            button_list[but_num].config(bg='#FF0000') #On affiche le point d'arriver en gris
            global destination
            destination = but_num
            destination_button['state'] = DISABLED
            type_elements = 0

    start_button = Button(frame_up, text='Point de départ', command=lambda: button_mode(1))
    obstacle_button = Button(frame_up, text='Ajouter des obstacles', command=lambda: button_mode(2))
    destination_button = Button(frame_up, text='Destination', command=lambda: button_mode(3))

    start_button.grid(row=0, column=3, sticky="ew", padx=10, pady=5)
    obstacle_button.grid(row=0, column=4, sticky="ew", padx=10, pady=5)
    destination_button.grid(row=0, column=5, sticky="ew", padx=10, pady=5)

    for i in range(20):
        for j in range(20):
            button_list.append(
                Button(frame_down, text=f'{count}', padx=5, pady=5, command=lambda x=count: boutous_cliques(x)))
            button_list[count].grid(row=i, column=j, sticky="ew")
            count += 1

    def solution():  # On utilise le script dans le fichier back.py
        parent = back.backened(depart, liste_obstacles, destination)
        for value in parent:
            button_list[value].config(bg='#0051FF')  # La couleur du chemin apparait en bleu
        button_list[depart].config(bg='#FFFF00')  # Le point de départ est affiché en jaune

    go_button = Button(frame_up, text='Commencer', command=solution)
    go_button.grid(row=0, column=6, padx=10, pady=5)

    def recommencer():
        root.destroy()
        Jeu()

    restart_button = Button(frame_up, text='Recommencer', command=recommencer)
    restart_button.grid(row=0, column=7, padx=10, pady=5)

    mainloop()


Jeu()
