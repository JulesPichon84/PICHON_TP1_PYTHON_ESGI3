
     __________          __  .__                   
     \______   \___.__._/  |_|  |__   ____   ____  
     |     ___<   |  |\   __\  |  \ /  _ \ /    \ 
     |    |    \___  | |  | |   Y  (  <_> )   |  \
     |____|    / ____| |__| |___|  /\____/|___|  /
               \/                \/            \/ 

# Bienvenue dans le TP1 consacré au langage de programmation Python.

## Vous trouverez dans ce dossier tous les éléments du TP:
   1. Le dossier *exo* --> Contient le code des différents exercices ainsi que les tests unitaires.
   2. Le dossier *Images* --> Conteint toutes les images pour l'interface utilisateur.
   3. Le dossier *Sound* --> Contient tous les sons pour l'interface utilisateur.

 ## Enfin vous avez deux fichiers .py à part:
   1. *interface.py* --> Permet de générer le menu ainsi que les différents exercices avec le module **Tkinter**.
   2. *main.py* --> C'est le point d'entrée du TP. Il appelle le fichier *interface.py*.


 Pour des raison de taille de fichier, l'exécutable du programme n'a pas pu être inclut.
 Si vous souhaitez avoir un exécutable sous Windows, il vous suffit d'exécuter le code suivant:
 ```
    pyinstaller --onefile main.py
 ```
 Si vous souhaitez avoir un exécutable sous Linux, il vous suffit d'exécuter le code suivant:
 ```
    pip install cx_Freeze
 ```
 Créer ensuite un fichier setup.py et placez les lignes de code suivantes:
 ```
    from cx_Freeze import setup, Executable

    setup(
         name="",
         version="",
         description="",
         executables=[Executable("main.py")])

    python setup.py build
```
 **Amusez-vous bien avec ce TP, et surtout n'oubliez pas d'activer le son de votre ordinateur !**
