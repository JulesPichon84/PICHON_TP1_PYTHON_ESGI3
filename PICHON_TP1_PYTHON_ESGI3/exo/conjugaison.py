# Importation du module Tkinter qui permet de créer une interface graphique.
# Importation du module verbecc qui est un module dédié à la conjugaison de verbes. 
from verbecc import Conjugator
from tkinter import *


# Définition de la fonction bescherelle qui va conjuguer notre verbe.
def bescherelle():
    verbe = entry.get().strip()  # Récupérer le texte de l'entrée utilisateur et supprimer les espaces.

    if verbe:
        try:
            cg = Conjugator(lang='fr')      # On sélectionne la langue.
            conjugaison = cg.conjugate(verbe)       # Notre verbe sera attribué à la variable "conjugaison".
            result_text.delete(1.0, END)        # Efface le texte précédent.
            result_text.insert(END, conjugaison)
        except Exception as e:      # Gestion des erreurs.
            result_text.delete(1.0, END)
            result_text.insert(END, f"Erreur : {str(e)}")
    else:
        result_text.delete(1.0, END)
        result_text.insert(END, "Veuillez entrer un VERBE valide !")


# Définition fonction principale.
def bescherelle_exercice(root):

    # Déclaration des variables globales.
    global entry, result_text

    exercise_frame = Frame(root)
    exercise_frame.pack(pady=20)

    # Définition police du texte.
    label = Label(exercise_frame, text="Bescherelle", font=("Arial", 14))
    label.pack()

    entry_label = Label(exercise_frame, text="Entrez un verbe :")
    entry_label.pack(pady=10)

    entry = Entry(exercise_frame)
    entry.pack()

     # Création bouton.
    check_button = Button(exercise_frame, text="Conjuguer le verbe", command=bescherelle)
    check_button.pack(pady=10)

    result_text = Text(exercise_frame, height=20, width=100)
    result_text.pack()

if __name__ == "__main__":
    root = Tk()
    root.title("Exercice Bescherelle")      # Titre de la fenêtre.
    root.geometry('800x400')        # Taille de la fenêtre si l'exercice est compilé sans le menu.
    bescherelle_exercice(root)
    root.mainloop()
