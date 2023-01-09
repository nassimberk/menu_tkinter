from tkinter import *

# Création de la fenêtre principale :
app = Tk()
app.title("Menu")
app.minsize(480, 360)
app.config(background="#4EE1D4")
app.iconbitmap("iconMenu.ico")

# Création la barre de menu:

menubarre = Menu(app)

# Création les menus principaux :

menuFichier = Menu(menubarre, tearoff=0)
menuHelp = Menu(menubarre, tearoff=0)

# Création un sous menu :
menuQuit = Menu(menuFichier, tearoff=0)

# Ajout les menus pricipale à la la barre de menu :

menubarre.add_cascade(label="Fichier", menu=menuFichier)
menubarre.add_cascade(label="Help", menu=menuHelp)


# Ajouter des commandes aux menu Fichier :
menuFichier.add_command(label="Nouveau")
menuFichier.add_command(label="Enregistrer")
menuFichier.add_command(label="Enregistret_sous")
menuFichier.add_command(label="Couper")
menuFichier.add_command(label="Copier")
menuFichier.add_command(label="Coller")
menuFichier.add_separator()

# Ajouter le sous menu au menu Fichier :

menuFichier.add_cascade(label="Quitter", menu=menuQuit)

# Ajouter des commandes au sous menu Quitter :
menuQuit.add_command(label="Non")
menuQuit.add_command(label="Oui", command=app.quit)



# Affficher le menu:

app.config(menu=menubarre)
app.mainloop()