# Importation du module Tkinter qui permet de créer une interface graphique.
from tkinter import *      


# Définition d'une fonction permettant d'inverser un mot.
def est_palindrome(mot):       
    return mot == mot[::-1]


# Pour la sécurité du code, on rajoute des vérification.
def traitement_mot(mot):       
    mot = mot.lower()        # On convertit le mot en minuscules et on retire les symboles spéciaux.
    if not mot.isalnum():
        raise ValueError("Le mot contient des caractères spéciaux.")
    return mot


# Définition de la fonction palindrome.
def verifier_palindrome():
    mot = entry.get()       # On récupère le mot passer en paramètre.
    result_label.config(text="")  # On réinitialise le texte du résultat à chaque vérification.
    if not mot:
        result_label.config(text="Veuillez entrer un mot.")
    else:
        try:
            mot = traitement_mot(mot)  # Appliquer la fonction traitement au mot.
            if est_palindrome(mot):
                result_label.config(text="Votre mot est un palindrome !")
            else:
                result_label.config(text="Votre mot n'est pas un palindrome.")
        except ValueError as e:     # Gestion d'erreurs.
            result_label.config(text=str(e))


# Définition de la fonction principale.
def palindrome_exercice(root):  

    # Déclaration des variables globales.
    global entry, result_label
    
    exercise_frame = Frame(root)
    exercise_frame.pack(pady=20)
    
    # Labels.
    label = Label(exercise_frame, text="Vérification de palindrome", font=("Arial", 14))
    label.pack()
    
    entry_label = Label(exercise_frame, text="Entrez un mot :")
    entry_label.pack(pady=10)
    
    entry = Entry(exercise_frame)
    entry.pack()

     # Création bouton.
    check_button = Button(exercise_frame, text="Vérifier", command=verifier_palindrome)     
    check_button.pack(pady=10)

     # Définition police du texte.
    result_label = Label(exercise_frame, text="", font=("Arial", 12))       
    result_label.pack()

# On appelle la fonction principale.
if __name__ == "__main__":      
    root = Tk()
    root.title("Exercice Palindrome")       # Titre de la fenêtre.
    root.geometry('400x200')        # Taille de la fenêtre si l'exercice est compilé sans le menu.
    palindrome_exercice(root)
    root.mainloop()
