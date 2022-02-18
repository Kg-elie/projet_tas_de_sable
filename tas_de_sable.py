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
from functools import partial
import tkinter as tk
import random as rd


#########################################
# definitions des constantes            #
#########################################
HEIGHT = 600
WIDTH = 600

#########################################
#  definitions des variables            #
#########################################
ligne = 50
l = []
#########################################
# definitions des fonctions             #
#########################################
def grillage(n,taille):
    """ cree une grille de n^2 case"""
    rythme = taille // n
    x = 0
    y = 0
    colors = ["black", "red","blue"]
    
    for i in range (n):
        x = 0
        for j in range(n):
            couleur = rd.choice(colors)
            canvas.create_rectangle((x,y),(x+rythme,y+rythme), fill=couleur ,outline=couleur )
            x += rythme
        y += rythme
       


def configuration(n):
    """remplie la grille d'une configuration aléatoire"""
    global l 
    l = []
    for i in range(n):
        a = []
        for j in range(n):
            a.append(rd.randint(0,3))
        l.append(list(a))
    
    
        

def  placement(n,taille):
    """place les nombre de grain de sables sur les widgets"""
    rythme = taille // n
    x = 0
    y = 0
    
    for i in l:
        x = 0
        for j in i:
            canvas.create_text((x+(rythme//2),y+(rythme//2)), text= j,fill="white")
            x += rythme
        y+= rythme

def construction_terrain(n,taille):
    """ construire le terrain à partir de plusieus fonctions"""
    
    grillage(n,taille)
    configuration(n)
    placement(n,taille)
    
    
#########################################
# programme principal
racine = tk.Tk()

canvas = tk.Canvas(racine,width= WIDTH, height= HEIGHT, bg= "black")
canvas.grid(column=0,row=0)


bouton = tk.Button(racine,text="configuration aléatoire",command=  partial( construction_terrain,ligne,HEIGHT))
bouton.grid(column=0,row=1)


racine.mainloop()
