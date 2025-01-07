from tkinter import *
from tkinter import messagebox

color = "white"
invcolor = "black"

# Initialisation de la fenêtre
fenetre = Tk()
version = "V0.5"
fenetre.title(f"Puissance 4, {version}, by BlueSkils")
fenetre.geometry("680x680")
fenetre.config(bg=color)

# Variables globales
grille = [[None for _ in range(10)] for _ in range(10)]  # 10 lignes, 10 colonnes
tour = 0
score_J1 = 2
score_J2 = 1

tour_text = StringVar()
tour_text.set("Au tour de Joueur 1")

c = Canvas(fenetre, width=600, height=580, bg=color)
c.pack()

tour_affiche = Label(fenetre, textvariable=tour_text, font=("Arial", 10, "bold"))
tour_affiche.place(x=20, y=635)


def draw():
    global color, invcolor
    c.delete("all")
    for i in range(11):
        c.create_line(50 + i * 50, 50, 50 + i * 50, 550, fill=invcolor, width=2)
        c.create_line(50, 50 + i * 50, 550, 50 + i * 50, fill=invcolor, width=2)

    for i in range(10):
        c.create_text(75 + i * 50, 25, text=str(i + 1), font=("Arial", 12, "bold"), fill=invcolor)

    for ligne in range(10):
        for colonne in range(10):
            if grille[ligne][colonne] is not None:
                Acolor = grille[ligne][colonne]
                x1, y1 = 50 + colonne * 50, 50 + ligne * 50
                x2, y2 = x1 + 50, y1 + 50
                c.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill=Acolor)

    # Mise à jour des scores et manche
    J1_score.config(text=f"Score du joueur n°1 : {score_J1}")
    J2_score.config(text=f"Score du joueur n°2 : {score_J2}")
    manche.config(text=f"Manche n°{score_J2 + score_J1 + 1}")


J1_score = Label(fenetre, text=f"Score du joueur n°1 : {score_J1}", bg=color, fg=invcolor)
J1_score.place(x=450, y=570)

J2_score = Label(fenetre, text=f"Score du joueur n°2 : {score_J2}", bg=color, fg=invcolor)
J2_score.place(x=450, y=590)

manche = Label(fenetre, text=f"Manche n°{score_J2 + score_J1 + 1}", font=("Arial", 9, "bold"), bg=color, fg=invcolor)
manche.place(x=450, y=620)


def recup_text(event=None):
    case = E.get()
    if case.isdigit():
        case_num = int(case)
        if 1 <= case_num <= 10:
            jouer(case_num)
        else:
            tour_text.set("Veuillez entrer un nombre valide entre 1 et 10.")
    else:
        tour_text.set("Veuillez entrer un nombre valide entre 1 et 10.")
    E.delete(0, END)


def jouer(case):
    global tour, score_J1, score_J2

    couleur_joueur = "red" if tour % 2 == 0 else "blue"
    prochain_joueur = "Joueur 2" if tour % 2 == 0 else "Joueur 1"
    tour_text.set(f"Au tour de {prochain_joueur}")

    colonne = case - 1
    if 0 <= colonne < 10:
        for ligne in range(9, -1, -1):
            if grille[ligne][colonne] is None:
                grille[ligne][colonne] = couleur_joueur
                x1, y1 = 50 + colonne * 50, 50 + ligne * 50
                x2, y2 = x1 + 50, y1 + 50
                c.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill=couleur_joueur)
                tour += 1

                if check_victory(ligne, colonne):
                    vainqueur = "Joueur 1 (Rouge)" if couleur_joueur == "red" else "Joueur 2 (Bleu)"
                    messagebox.showinfo("Victoire", f"Félicitations ! {vainqueur} a gagné !")
                    if couleur_joueur == "red":
                        score_J1 += 1
                    else:
                        score_J2 += 1
                    reset_game()
                elif tour == 100:
                    messagebox.showinfo("Match nul", "Le jeu est terminé en match nul.")
                    reset_game()
                return
        tour_text.set("Cette colonne est pleine. Choisissez une autre colonne.")
    else:
        tour_text.set("Le nombre saisi est incorrect. Veuillez entrer un nombre entre 1 et 10.")
    check_victory()


def check_victory(row, col):
    # Détermine la couleur du joueur actuel
    player_color = grille[row][col]
    if not player_color:
        return False

    directions = [
        (1, 0),   # Vertical
        (0, 1),   # Horizontal
        (1, 1),   # Diagonale descendante
        (1, -1)   # Diagonale montante
    ]

    for dr, dc in directions:
        count = 1  # Compte le jeton actuel

        # Vérifie dans la direction positive
        r, c = row + dr, col + dc
        while 0 <= r < 10 and 0 <= c < 10 and grille[r][c] == player_color:
            count += 1
            r += dr
            c += dc

        # Vérifie dans la direction négative
        r, c = row - dr, col - dc
        while 0 <= r < 10 and 0 <= c < 10 and grille[r][c] == player_color:
            count += 1
            r -= dr
            c -= dc

        if count >= 4:
            return True

    return False


def reset_game():
    global grille, tour
    grille = [[None for _ in range(10)] for _ in range(10)]
    tour = 0
    tour_text.set("Au tour de Joueur 1")
    draw()


def changecolor():
    global color, invcolor
    if color == "white":
        color = "black"
        invcolor = "white"
    else:
        color = "white"
        invcolor = "black"

    fenetre.config(bg=color)
    c.config(bg=color)

    tour_affiche.config(bg=color, fg=invcolor)
    L_1.config(bg=color, fg=invcolor)
    E.config(bg=color, fg=invcolor, insertbackground=invcolor)
    B_1.config(bg=color, fg=invcolor)
    B_color.config(bg=color, fg=invcolor)
    J1_score.config(bg=color, fg=invcolor)
    J2_score.config(bg=color, fg=invcolor)
    manche.config(bg=color, fg=invcolor)

    draw()


L_1 = Label(fenetre, text="Entrez votre nombre :", bg=color, fg=invcolor)
L_1.place(x=20, y=600)

E = Entry(fenetre)
E.place(x=150, y=600)
E.bind('<Return>', recup_text)

B_1 = Button(fenetre, text="Valider", command=recup_text, bg=color, fg=invcolor)
B_1.place(x=250, y=600)

B_color = Button(fenetre, text="Changer de mode", command=changecolor, bg=color, fg=invcolor)
B_color.place(x=250, y=635)

draw()
fenetre.mainloop()
