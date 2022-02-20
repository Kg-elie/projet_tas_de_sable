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
ligne = 100
l = []
case_id = []
#########################################
# definitions des fonctions             #
#########################################
def grillage(n,taille):
    global case_id
    """ cree une grille de n^2 case"""
    if len(case_id) > 0:
        case_id = []
    
    rythme = taille // n
    x = 2
    y = 2
    
    for i in range (n):
        x = 2
        for j in range(n):
            case_id.append(canvas.create_rectangle((x,y),(x+rythme,y+rythme), fill="black" ,outline="white", width= 2 ))
            x += rythme
        y += rythme
    id = 0
    
    for i in l:
        for j in i:
            if j == 0:
                canvas.itemconfig(case_id[id], fill ="blue")
            elif j == 1:
                canvas.itemconfig(case_id[id], fill="red")
            elif j == 2:
                canvas.itemconfig(case_id[id], fill="green")
            elif j == 3:
                canvas.itemconfig(case_id[id], fill="purple")
            id += 1
    


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
    

    configuration(n)
    grillage(n,taille)
    #placement(n,taille)

    
def change_couleurs():
    global case_id
    id = 0
    
    for i in l:
        for j in i:
            if j == 0:
                canvas.itemconfig(case_id[id], fill ="blue")
            elif j == 1:
                canvas.itemconfig(case_id[id], fill="red")
            elif j == 2:
                canvas.itemconfig(case_id[id], fill="green")
            elif j == 3:
                canvas.itemconfig(case_id[id], fill="purple")
            id += 1
    
#########################################
# programme principal
racine = tk.Tk()

canvas = tk.Canvas(racine,width= WIDTH, height= HEIGHT, bg= "black")
canvas.grid(column=0,row=0)


bouton = tk.Button(racine,text="configuration aléatoire",command=  lambda : construction_terrain(ligne,HEIGHT))
bouton.grid(column=0,row=1)

bouton = tk.Button(racine,text="couleurs",command= change_couleurs)
bouton.grid()


racine.mainloop()

