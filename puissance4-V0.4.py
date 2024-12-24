from tkinter import *

color = "white"
invcolor = "black"

# Initialisation de la fenêtre
fenetre = Tk()
version = "V0.2"
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

    J1_score = Label(fenetre, text=f"Score du joueur n°1 : {score_J1}", bg=color, fg=invcolor)
    J1_score.place(x=450, y=570)

    J2_score = Label(fenetre, text=f"Score du joueur n°2 : {score_J2}", bg=color, fg=invcolor)
    J2_score.place(x=450, y=590)

    manche = Label(fenetre, text=f"Manche n°{score_J2 + score_J1 + 1}", font=("Arial", 9, "bold"), bg=color, fg=invcolor)
    manche.place(x=450, y=620)



    for i in range(10):
        c.create_text(75 + i * 50, 25, text=str(i + 1), font=("Arial", 12, "bold"), fill = invcolor)

def recup_text(event=None):
    case = E.get()
    if int(case) >0 and int(case) <11:
        jouer(int(case))
    else:
        tour_text.set("Veuillez entrer un nombre valide entre 1 et 10.")
    E.delete(0, END)

def jouer(case):
    global tour

    color = "red" if tour % 2 == 0 else "blue"
    tour_text.set("Au tour de Joueur 2" if tour % 2 == 0 else "Au tour de Joueur 1")

    colonne = case - 1
    if 0 <= colonne < 10:
        for ligne in range(9, -1, -1):
            if grille[ligne][colonne] is None:
                grille[ligne][colonne] = color
                x1, y1 = 50 + colonne * 50, 50 + ligne * 50
                x2, y2 = x1 + 50, y1 + 50
                c.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill=color)
                tour += 1
                return
        tour_text.set("Cette colonne est pleine. Choisissez une autre colonne.")
    else:
        tour_text.set("Le nombre saisie est incorrect. Veuillez entrer un nombre entre 1 et 10.")


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

    draw()



L_1 = Label(fenetre, text="Entrez votre nombre :")
L_1.place(x=20, y=600)

E = Entry(fenetre)
E.place(x=150, y=600)
E.bind('<Return>', recup_text)

B_1 = Button(fenetre, text="Valider", command=lambda: recup_text())
B_1.place(x=250, y=600)

B_color = Button(fenetre, text="Changer de mode", command=changecolor)
B_color.place(x=250, y=635)


draw()
fenetre.mainloop()
