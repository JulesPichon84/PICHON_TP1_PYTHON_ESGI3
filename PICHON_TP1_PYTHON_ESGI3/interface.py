 # Importation du module Tkinter qui permet de créer une interface graphique, PIL pour gérer les photos et pygame pour les sons.
from tkinter import *
from PIL import Image, ImageTk
from exo import calculatrice, devise, factorielle, palindrome, conjugaison
import pygame


def main():
# Création de la fenêtre principale.
    root = Tk()
    root.title("MENU PYTHON TP1 - Jules PICHON - ESGI3")
    root.geometry('1200x700')


# Redimensionne l'image de fond pour s'adapter à la taille de la fenêtre.
    def resize_image(event):   
        new_width = event.width
        new_height = event.height
        resized_image = background_image.resize((new_width, new_height), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_image)


# Charge l'image de fond
    background_image = Image.open("Images/background.jpg") 
    background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
    background_photo = ImageTk.PhotoImage(background_image)


# Lie la fonction de redimensionnement à l'événement de redimensionnement de la fenêtre
    root.bind("<Configure>", resize_image)


# Initialisation de pygame.
    pygame.mixer.init()


# Charge et joue de la musique sur la page d'accueil.
    pygame.mixer.music.load("Sound/minecraft_main_theme.mp3")
    pygame.mixer.music.play(-1)  # Joue en boucle (-1 signifie en boucle infinie).


    def play_sound(sound_file):
        sound = pygame.mixer.Sound(sound_file)
        sound.play()


# Création d'un label pour afficher l'image de fond
    background_label = Label(root, image=background_photo)
    background_label.place(relwidth=1, relheight=1)
    background_label.photo = background_photo


# Création d'un cadre (Frame) pour organiser le contenu.
    frame = Frame(root)
    frame.pack(expand=True)


# Création d'un label avec le texte centré.
    label = Label(frame, text="Bienvenue dans le menu du TP1 consacré au langage de programmation Python !\nVoici la liste des exercices disponibles :\n", font=("Arial", 14))
    label.grid(row=0, column=0, columnspan=5, pady=0)  # On ajoute un espace en haut et en bas.


# Création d'un sous-cadre (Frame) pour les boutons et les centrer.
    button_frame = Frame(frame)
    button_frame.grid(row=1, column=0, columnspan=5)


# Liste des noms de fichiers d'images pour chaque exercice
    images = ["Images/image1.jpg", "Images/image2.jpg", "Images/image3.png", "Images/image4.png", "Images/image5.jpg"]


# Fonction pour lancer un exercice dans une nouvelle fenêtre (Toplevel).
    def run_exercise(main_function, image_index):
        exercise_window = Toplevel(root)  # Création d'une nouvelle fenêtre.
        exercise_window.title("Exercice")  # Donne un titre à la fenêtre.
        exercise_window.geometry('900x700')  # Définition taille de la fenêtre.

    # Charge l'image spécifique pour l'exercice.
        exercise_image = Image.open(images[image_index])
        exercise_image = exercise_image.resize((800, 400), Image.ANTIALIAS)
        exercise_photo = ImageTk.PhotoImage(exercise_image)

    # Affiche l'image dans la nouvelle fenêtre.
        exercise_label = Label(exercise_window, image=exercise_photo)
        exercise_label.pack(fill=BOTH, expand=True)
        exercise_label.image = exercise_photo

    # Exécution de la fonction principale de l'exercice dans la nouvelle fenêtre.
        main_function(exercise_window)


# Création d'un bouton pour chaque exercice et association d'un son et d'une image à un bouton.
    btn1 = Button(button_frame, text="Une calculatrice sous Python ?", command=lambda: (play_sound("Sound/huh.mp3"),run_exercise(calculatrice.calculatrice_exercice, 0)))
    btn2 = Button(button_frame, text="Calculs magiques", command=lambda: (play_sound("Sound/wii.mp3"), run_exercise(factorielle.factorielle_exercice, 1)))
    btn3 = Button(button_frame, text="Bescherelle", command=lambda: (play_sound("Sound/ez.mp3"), run_exercise(conjugaison.bescherelle_exercice, 2)))
    btn4 = Button(button_frame, text="Taux de change de monnaie", command=lambda: (play_sound("Sound/bully.mp3"), run_exercise(devise.devise_exercice, 3)))
    btn5 = Button(button_frame, text="Exercice Palindrome", command=lambda: (play_sound("Sound/xp.mp3"), run_exercise(palindrome.palindrome_exercice, 4)))


# On met les boutons sur la même ligne.
    btn1.grid(row=0, column=0, padx=10)
    btn2.grid(row=0, column=1, padx=10)
    btn3.grid(row=0, column=2, padx=10)
    btn4.grid(row=0, column=3, padx=10)
    btn5.grid(row=0, column=4, padx=10)


# Centrer le sous-cadre (Frame) des boutons.
    button_frame.grid_columnconfigure(0, weight=1)  # Permet d'étirer la colonne.


# On démarre la boucle d'évènements.
    root.mainloop()

if __name__ == "__main__":
    main()
