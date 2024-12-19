from tkinter import *


# Déclaration des variables
fenetre = Tk()
version = "V0.2"
fenetre.title(f"Puissance 4, {version}, by BlueSkils")
fenetre.geometry("650x650")

tour = 0
color = 0

score_J1 = 10
score_J2 = 3

# Création des étiquettes pour le tour et le score
tour_text = StringVar()
tour_text.set("Au tour de Joueur 1")

c = Canvas(fenetre, width=550, height=550, bg="ivory")
c.pack()

tour_affiche = Label(fenetre, textvariable= tour_text)
tour_affiche.place(x = 120, y = 600)
print(f" Au tour de Joueur 1")

def draw():

    # Dessiner la grille
    for i in range(11): 
        c.create_line(50+i*50, 50, 50+i*50, 550, fill="black", width=2)
        c.create_line(50, 50+i*50, 550, 50+i*50, fill="black", width=2)

    
    J1_score = Label(fenetre, text=f"Score du joueur n°1 : {score_J1} ")
    J1_score.place(x = 450, y = 570)

    J2_score = Label(fenetre, text=f"Score du joueur n°2 : {score_J2} ")
    J2_score.place(x = 450, y = 600)

    
    # Ajouter des étiquettes pour les colonnes (A à J)
    for i in range(10):
        c.create_text(75+i*50, 25, text=str(i+1), font=("Arial", 12, "bold"))  # Chiffres 




def jouer():
    global tour, tour_affiche, tour_text

    if int(tour) %2 == 0:
        color = "red"
        tour_text.set("Au tour de Joueur 2")

    else:
        color = "blue"
        tour_text.set("Au tour de Joueur 1")


    case = E.get()

    # Récupération des coordonnées de la case
    chiffre = int(case[0])
    if len(case)>2:
        chiffre += 9

    # Vérification des coordonnées
    if chiffre < 1 or chiffre > 10:
        raise ValueError("Coordonnées invalides")

    # Modification de la case
    c.create_rectangle(50*chiffre, 500 , (50*chiffre)+50, 550 ,fill=color)

    tour += 1   
    print("Action Ok")
    
    
L_1 = Label(fenetre, text = "Entrez votre nombre :")
L_1.place(x = 20, y = 570)

E = Entry(fenetre)
E.place(x = 150, y = 570)

B_1 = Button(fenetre, text = "Valider", command=jouer)
B_1.place(x = 250, y = 570)

draw()
fenetre.mainloop()