#from glob import glob
#from re import L    
from tkinter import *


# Déclaration des variables
fenetre = Tk()
version = "V0.1"
fenetre.title(f"Puissance 4, {version}, by BlueSkils")
fenetre.geometry("650x650")

tour = 0
color = 0

score_J1 = 10
score_J2 = 3

c = Canvas(fenetre, width=550, height=550, bg="ivory")
c.pack()

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
        c.create_text(75+i*50, 25, text=str(i+1), font=("Arial", 12, "bold"))  # Lettres 
        c.create_text(25, 75+i*50, text=chr(65+i), font=("Arial", 12, "bold"))  # Chiffres  
    


def jouer():
    global tour

    if int(tour) %2 == 0:
        color = "red"
    else:
        color = "blue"
    tour += 1
    case = E.get()

    # Récupération des coordonnées de la case
    lettre = case[0].upper()
    chiffre = int(case[1])
    if len(case)>2:
        chiffre += 9

    # Vérification des coordonnées
    if lettre < 'A' or lettre > 'J' or chiffre < 1 or chiffre > 10:
        raise ValueError("Coordonnées invalides")

    # Modification de la case
    c.create_rectangle(50*chiffre, (ord(lettre)-64)*50 , (50*chiffre)+50, ((ord(lettre)-64)*50)+50 ,fill=color)

    print("Action Ok")
    
    
L_1 = Label(fenetre, text = "Entrez votre nombre :")
L_1.place(x = 20, y = 570)

E = Entry(fenetre)
E.place(x = 150, y = 570)

B_1 = Button(fenetre, text = "Valider", command=jouer)
B_1.place(x = 250, y = 570)

draw()
fenetre.mainloop()