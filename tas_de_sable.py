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
import random as rd


#########################################
# definitions des constantes            #
#########################################
HEIGHT = 1000
WIDTH = 1000

#########################################
#  definitions des variables            #
#########################################
ligne = 100
l = []
#########################################
# definitions des fonctions             #
#########################################
def grillage(n,taille):
    """ cree une grille de n^2 case"""
    rythme = taille // n
    x = 0
    y = 0
    
    for i in range (n):
        x = 0
        for j in range(n):
            canvas.create_rectangle((x,y),(x+rythme,y+rythme), fill= "red",outline="white" )
            x += rythme
        y += rythme
       


def configuration(n):
    """remplie la grille d'une configuration aléatoire"""
    global l 
    for i in range(n):
        a = []
        for j in range(n):
            a.append(rd.randint(0,5))
        l.append(list(a))
    for i in l:
        print(i)
        

def  placement(n,taille):
    rythme = taille // n
    x = 0
    y = 0
    
    for i in l:
        x = 0
        for j in i:
            canvas.create_text((x+(rythme//2),y+(rythme//2)), text= j,fill="white")
            x += rythme
        y+= rythme


#########################################
# programme principal
racine = tk.Tk()

canvas = tk.Canvas(racine,width= WIDTH, height= HEIGHT, bg= "black")
canvas.grid(column=0,row=0)
grillage(ligne,1000)
configuration(ligne)
placement(ligne,1000)

bouton = tk.Button(racine,text="bouton")

bouton.grid(column=0,row=1)


racine.mainloop()
