# Importation du module Tkinter qui permet de créer une interface graphique.
from tkinter import *


# Création d'un dictionnaire pour nos monnaies.
taux_de_conversion = {
    ('euro', 'dollar'): 1.049, ('euro', 'livre'): 0.86, ('euro', 'yen'): 156.76, ('euro', 'francsuisse'): 0.97, ('euro', 'rouble'): 101.5,
    ('dollar', 'euro'): 0.95, ('dollar', 'livre'): 0.82, ('dollar', 'yen'): 148.73, ('dollar', 'francsuisse'): 0.91, ('dollar', 'rouble'): 96.92,
    ('livre', 'euro'): 1.15, ('livre', 'dollar'): 1.22, ('livre', 'yen'): 182, ('livre', 'francsuisse'): 1.115, ('livre', 'rouble'): 118.6,
    ('yen', 'euro'): 0.0063, ('yen', 'dollar'): 0.0067, ('yen', 'livre'): 0.0055, ('yen', 'francsuisse'): 0.0061, ('yen', 'rouble'): 0.652,
    ('francsuisse', 'euro'): 1.03, ('francsuisse', 'dollar'): 1.098, ('francsuisse', 'livre'): 0.897, ('francsuisse', 'yen'): 163.3, ('francsuisse', 'rouble'): 106.57,
    ('rouble', 'euro'): 0.0098, ('rouble', 'dollar'): 0.010, ('rouble', 'livre'): 0.0084, ('rouble', 'yen'): 1.53, ('rouble', 'francsuisse'): 0.0093
}


# Définition d'une fonction de calcul des conversions.
def convertir_devises(montant, source, cible):
    if (source, cible) in taux_de_conversion:
        taux = taux_de_conversion[(source, cible)]
        resultat = montant * taux
        return resultat
    else:
        raise ValueError("Conversion non prise en charge")


# Définition d'une fonction qui récupère les différentes données.
def convertir():
    source = source_var.get()
    cible = cible_var.get()
    montant = float(montant_entry.get())   
    try:
        resultat = convertir_devises(montant, source, cible)
        resultat_label.config(text=f"Résultat: {resultat} {cible.upper()}")
    except ValueError as e:     # Gestion d'erreurs.
        resultat_label.config(text=f"Erreur : {e}")


# Définition de la fonction principale.
def devise_exercice(root):

    # Déclaration des variables globales.
    global resultat_label, source_var, cible_var, montant_entry

     # Labels.
    source_label = Label(root, text="Devise source:")
    source_label.pack()

    # Options pour la devise source
    sources = ['euro', 'dollar', 'livre', 'yen', 'francsuisse', 'rouble']
    source_var = StringVar(root)
    source_var.set(sources[0])  # Définir la première option comme valeur par défaut

    source_menu = OptionMenu(root, source_var, *sources)
    source_menu.pack()

    cible_label = Label(root, text="Devise cible:")
    cible_label.pack()

    # Options pour la devise cible.
    cibles = ['euro', 'dollar', 'livre', 'yen', 'francsuisse', 'rouble']
    cible_var = StringVar(root)
    cible_var.set(cibles[1])  # Définir la deuxième option comme valeur par défaut.

    # Ajout d'un menu déroulant pour les choix de devise.
    cible_menu = OptionMenu(root, cible_var, *cibles)       # (*cibles) ==> Chaque élément de la liste "cibles" devient un choix dans le menu déroulant.
    cible_menu.pack()

    montant_label = Label(root, text="Montant:")
    montant_label.pack()

    montant_entry = Entry(root)
    montant_entry.pack()

     # Création bouton.
    convert_button = Button(root, text="Convertir", command=convertir)
    convert_button.pack()

    # Définition police du texte.
    resultat_label = Label(root, text="")
    resultat_label.pack()


# On appelle la fonction principale.
if __name__ == "__main__":
    root = Tk()
    root.title("Convertisseur de devises")      # Titre de la fenêtre.
    root.geometry('500x300')        # Taille de la fenêtre si l'exercice est compilé sans le menu.
    devise_exercice(root)
    root.mainloop()
