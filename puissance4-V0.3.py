from tkinter import *

# Initialisation de la fenêtre
fenetre = Tk()
version = "V0.2"
fenetre.title(f"Puissance 4, {version}, by BlueSkils")
fenetre.geometry("650x650")

# Variables globales
grille = [[None for _ in range(10)] for _ in range(10)]  # 10 lignes, 10 colonnes
tour = 0
score_J1 = 2
score_J2 = 1

tour_text = StringVar()
tour_text.set("Au tour de Joueur 1")

c = Canvas(fenetre, width=550, height=550, bg="ivory")
c.pack()

tour_affiche = Label(fenetre, textvariable=tour_text)
tour_affiche.place(x=120, y=600)

def draw():
    for i in range(11):
        c.create_line(50 + i * 50, 50, 50 + i * 50, 550, fill="black", width=2)
        c.create_line(50, 50 + i * 50, 550, 50 + i * 50, fill="black", width=2)

    J1_score = Label(fenetre, text=f"Score du joueur n°1 : {score_J1}")
    J1_score.place(x=450, y=570)

    J2_score = Label(fenetre, text=f"Score du joueur n°2 : {score_J2}")
    J2_score.place(x=450, y=590)

    manche = Label(fenetre, text=f"Manche n°{score_J2 + score_J1 + 1}", font=("Arial", 9, "bold"))
    manche.place(x=450, y=620)

    for i in range(10):
        c.create_text(75 + i * 50, 25, text=str(i + 1), font=("Arial", 12, "bold"))

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

L_1 = Label(fenetre, text="Entrez votre nombre :")
L_1.place(x=20, y=570)

E = Entry(fenetre)
E.place(x=150, y=570)
E.bind('<Return>', recup_text)

B_1 = Button(fenetre, text="Valider", command=lambda: recup_text())
B_1.place(x=250, y=570)

draw()
fenetre.mainloop()
