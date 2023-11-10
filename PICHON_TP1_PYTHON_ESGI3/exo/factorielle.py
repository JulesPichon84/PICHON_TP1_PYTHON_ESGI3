# Importation du module Tkinter qui permet de créer une interface graphique.
from tkinter import *


# Définition d'une fonction somme.
def somme(x):
    return sum(range(x + 1))


# Définition d'une fonction factorielle.
def factorielle(x):
    if x < 0:       # Vérification
        raise ValueError("Erreur, le nombre entier rentré n'est pas bon !")
    elif x == 0:
        return 1
    else:
        fact = 1
        for i in range(1, x + 1):
            fact *= i
        return fact


# Définition de la fonction qui va calculer et renvoyer les résultats.
def calculer():
    nombre = entry.get()       # On récupère le nombre passer en paramètre.
    if nombre.isdigit():        # Vérification pour que le nombre entré soit bien un nombre.
        x = int(nombre)         # On n'autorise que les nombres entiers.
        somme_result.set(f"La somme de {x} est : {'+'.join(map(str, range(1, x+1)))} = {somme(x)}")
        factorielle_result.set(f"La factorielle de {x} est : {'*'.join(map(str, range(1, x+1)))} = {factorielle(x)}")
    else:
        somme_result.set("Erreur : Entrez un nombre entier valide.")


# Définition de la fonction principale.
def factorielle_exercice(root):

    # Déclaration des variables globales.
    global entry, somme_result, factorielle_result  

    # Création d'une fenêtre.
    frame = Frame(root)
    frame.pack(pady=20)

    label = Label(frame, text="Calcul de somme et de factorielle", font=("Arial", 14))
    label.pack()

    entry_label = Label(frame, text="Entrez un nombre :")
    entry_label.pack(pady=10)

    entry = Entry(frame)
    entry.pack()

     # Création bouton.
    calculate_button = Button(frame, text="Calculer", command=calculer)
    calculate_button.pack(pady=10)

    somme_result = StringVar()
    factorielle_result = StringVar()

    # Définition police du texte.
    result_label1 = Label(frame, textvariable=somme_result, font=("Arial", 12))
    result_label1.pack()

    result_label2 = Label(frame, textvariable=factorielle_result, font=("Arial", 12))
    result_label2.pack()


# On appelle la fonction principale.
if __name__ == "__main__":
    root = Tk()
    root.title("Calcul de somme et de factorielle")     # Titre de la fenêtre.
    root.geometry('500x300')        # Taille de la fenêtre si l'exercice est compilé sans le menu.
    factorielle_exercice(root)
    root.mainloop()
