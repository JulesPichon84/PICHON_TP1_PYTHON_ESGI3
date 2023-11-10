# Importation du module Tkinter qui permet de créer une interface graphique.
from tkinter import *


# Définition fonction addition.
def addition(x, y):
    return x + y


# Définition fonction soustraction.
def soustraction(x, y):
    return x - y


# Définition fonction multiplication.
def multiplication(x, y):
    return x * y


# Définition fonction division.
def division(x, y):
    if y == 0:
        raise ValueError("Erreur de calcul, nous ne pouvons pas diviser par zéro !")
    return x / y


# Définition de la fonction calculette.
def calculette():
    operation = operation_entry.get().upper()
    x = float(x_entry.get())
    y = float(y_entry.get())

    # Liste des opérations disponibles.
    operations = {
        'A': addition,
        'S': soustraction,
        'M': multiplication,
        'D': division
    }

    if operation in operations:
        try:
            resultat = operations[operation](x, y)
            resultat_label.config(text=f"Résultat : {resultat}")
        except ValueError as e:
            resultat_label.config(text=str(e))
    else:
        resultat_label.config(text="Opération invalide")


# Définition de la fonction principale.
def calculatrice_exercice(root):

    # Déclaration des variables globales.
    global operation_entry, x_entry, y_entry, resultat_label
    
    frame = Frame(root)
    frame.pack(pady=20)

    label = Label(frame, text="Calculatrice Python", font=("Arial", 14))
    label.pack()

    operation_label = Label(frame, text="Voici les opérations disponibles:\n \n- Addition (A)\n - Soustraction (S)\n - Multiplication (M)\n - Division (D)\n")
    operation_label.pack(pady=10)

    operation_entry = Entry(frame)
    operation_entry.pack()

    x_label = Label(frame, text="Nombre x :")
    x_label.pack(pady=10)

    x_entry = Entry(frame)
    x_entry.pack()

    y_label = Label(frame, text="Nombre y :")
    y_label.pack(pady=10)

    y_entry = Entry(frame)
    y_entry.pack()

     # Création bouton.
    calculate_button = Button(frame, text="Calculer", command=calculette)
    calculate_button.pack(pady=10)

    # Définition police du texte.
    resultat_label = Label(frame, text="", font=("Arial", 12))
    resultat_label.pack()


# On appelle la fonction principale.
if __name__ == "__main__":
    root = Tk()
    root.title("Calculatrice")      # Titre de la fenêtre.
    root.geometry('500x500')        # Taille de la fenêtre si l'exercice est compilé sans le menu.
    calculatrice_exercice(root)
    root.mainloop()

