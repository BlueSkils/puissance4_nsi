from tkinter import *
from tkinter import colorchooser


# Déclaration des variables
fenetre = Tk()
version = "V0.2"
fenetre.title(f"Bataille Navale {version}, by BlueSkils")
fenetre.geometry("650x650")
#fenetre.iconbitmap('1.png')

color = ""

label = Label(fenetre, text=f"Bataille Navale {version} !")
label.pack()



c = Canvas(fenetre, width=550, height=550)  # Ajusté pour inclure les étiquettes mais rajouter , bg="ivory" si besoin d'un fond
c.pack()

# Fonctions d'aide
def drawn(c):

    # Dessiner la grille
    for i in range(11): 
        c.create_line(50+i*50, 50, 50+i*50, 550, fill="black", width=2)
        c.create_line(50, 50+i*50, 550, 50+i*50, fill="black", width=2)

    # Ajouter des étiquettes pour les colonnes (A à J)
    for i in range(10):
        c.create_text(75+i*50, 25, text=str(i+1), font=("Arial", 12, "bold"))  # Lettres 
        c.create_text(25, 75+i*50, text=chr(65+i), font=("Arial", 12, "bold"))  # Chiffres  



def tir():
    global color

    case = input("Choississez une case :\n ")

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
    print(f"Color = {color}")

    print("Action Ok")
    
    tir()

def changecolor():
    global color
    color = colorchooser.askcolor(title ="Choississez une couleur")[1]



def suppr(event):
    clic = event.x, event.y
    bord = c.find_closest(*clic)
    c.delete(bord)

def quitter(event):
    if event.char == "a":
        fenetre.destroy()

# Liaisons des événements
c.bind("<Button-1>", suppr)
fenetre.bind("<Key>", quitter) 

button = Button(fenetre, text = "Select color", command = changecolor)
button.pack()


# Lancement de la fenêtre et des fonctions de bases
print(f"Lancement de Bataille Navale {version}")
drawn(c)
tir()
fenetre.mainloop()