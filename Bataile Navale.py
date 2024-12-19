#BIBLIOTHEQUES

from tkinter import *

#definition des variables
grille = [[" " for i in range(11)] for j in range(11)]

#nom des colones
for j in range(1,len(grille[0])):
    grille[0][j] = str(j)
    
#nom des lignes   
for i in range(1,len(grille[1])):
    grille[i][0]= chr(64+i)
    

#fonctions d'aide

def dummy():
    print("pouet")


def afficheur(grille):
    for ligne in grille:
        print(ligne)

def tir(chaine):
    global grille
    nom_ligne = chaine[0]
    nom_colone = chaine[1:]
    for i in range(1,len(grille[1])):
        for j in range(1,len(grille[1])):
            if grille[i][0] == nom_ligne and grille[0][j] == nom_colone:
                grille[i][j] = "x"


def shoot():
    global grille, canevas
    chaine = E.get()
    tir(chaine)
    draw(canevas)
    afficheur(grille)

def draw(canevas):
    
    TAILLE_GRILLE = 11
    TAILLE_CASE = 50    
    for i in range(TAILLE_GRILLE + 1):
        canevas.create_line(0, i * TAILLE_CASE, TAILLE_GRILLE * TAILLE_CASE, i * TAILLE_CASE, fill="black")
        canevas.create_line(i * TAILLE_CASE, 0, i * TAILLE_CASE, TAILLE_GRILLE * TAILLE_CASE, fill="black")
    for i in range(1,len(grille[1])):
        for j in range(1,len(grille[1])):
            if grille[j][i] == "x":
                canevas.create_rectangle(i * TAILLE_CASE,j * TAILLE_CASE,(i+1) * TAILLE_CASE,(j+1) * TAILLE_CASE, fill="black")
                
                

#boucle principale

fenetre = Tk()
fenetre.title("Bataille Navale")
fenetre.geometry('550x600')

canevas = Canvas(fenetre, width = 550, height = 550,bg="lightblue")
canevas.pack()


draw(canevas)
    
L_1 = Label(fenetre, text = "Entrez votre nombre :")
L_1.place(x = 20, y = 570)

E = Entry(fenetre)
E.place(x = 150, y = 570)

B_1 = Button(fenetre, text = "Valider",command=shoot)
B_1.place(x = 250, y = 570)

fenetre.mainloop()

 


