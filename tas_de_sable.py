#########################################
# groupe BI TD 1
# Elie KANGA
# Sarah Medeneche
# Iram MADANI FOUATIH
#  https://github.com/uvsq22101259/projet_tas_de_sable
#########################################

#########################################
# importation librairie                 #
#########################################
import tkinter as tk

#########################################
# definitions des constantes            #
#########################################
HEIGHT = 600
WIDTH = 600

#########################################
#  definitions des variables            #
#########################################


#########################################
# definitions des fonctions             #
#########################################
def grillage(n,taille):
    """ cree une grille de n^n case"""
    rythme = taille // n
    x = rythme
    y = rythme 
    
    for i in range (n):
        canvas.create_line((0,y),(600,y), fill= "white")
    
        canvas.create_line((x,0),(x,600), fill= "white")
        x += rythme
        y += rythme

#########################################
# programme principal
racine = tk.Tk()

canvas = tk.Canvas(racine,width= WIDTH, height= HEIGHT, bg= "black")
canvas.grid(column=0,row=0)
grillage(60,600)

bouton = tk.Button(racine,text="bouton")
bouton.grid(column=0,row=1)


racine.mainloop()
