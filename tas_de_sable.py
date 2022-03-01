#########################################
# groupe BI TD 1
# Elie KANGA
# Sarah Medeneche
# Iram MADANI FOUATIH
# https://github.com/uvsq22101259/projet_tas_de_sable
#########################################

#########################################
# importation librairie                 #
#########################################

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
# coisir une ligne qui ne fit pas de decimale si l'on divise la taille par elle
ligne =4
# matrice contenant les grain de sable pour chaque case
l = []
# liste contenant les identifiants de chaque case
case_id = []
#########################################
# definitions des fonctions             #
#########################################
def grillage(n,taille):
    global case_id
    """ cree une grille de n^2 case, et donne a chaque case une couleur selectionner en fonction du grain de sable qu'elle contient """
    if len(case_id) > 0:
        for i in case_id:
            canvas.delete(i)
        case_id = []
    
    rythme = taille // n
    x = 0
    y = 3
    
    for i in range (n):
        x = 3
        for j in range(n):
            case_id.append(canvas.create_rectangle((x,y),(x+rythme,y+rythme), fill="black" ,outline="black", width= 2 ))
            x += rythme
        y += rythme
    id = 0
    
    for i in l:
        for j in i:
            if j == 0:
                canvas.itemconfig(case_id[id], fill ="grey")
            elif j == 1:
                canvas.itemconfig(case_id[id], fill="purple")
            elif j == 2:
                canvas.itemconfig(case_id[id], fill="blue")
            elif j == 3:
                canvas.itemconfig(case_id[id], fill="cyan")
            elif j >= 4:
                canvas.itemconfig(case_id[id], fill="yellow")
            id += 1
    

def configuration(n):
    """remplie la grille d'une configuration aléatoire"""
    global l 
    l = []
    for i in range(n):
        a = []
        for j in range(n):
            a.append(rd.randint(0,4))
        l.append(list(a))
    print(l)
          

def  placement(n,taille):
    """place les nombres de grain de sables sur les widgets"""
    rythme = taille // n
    x = 0
    y = 3
    
    for i in l:
        x = 3
        for j in i:
            canvas.create_text((x+(rythme//2),y+(rythme//2)), text= j,fill="white")
            x += rythme
        y+= rythme


def construction_terrain(n,taille):
    """ construire le terrain à partir de plusieus fonctions"""
    

    configuration(n)
    grillage(n,taille)
    placement(n,taille)

    
def ecoulement(n,taille):
    """simule un ecoulement en donnant a chaque case voisine un grain de sabke si la case est surchargée"""
    global case_id, l
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j]>= 4 and (j > 0) and (i > 0) and (j < n-1) and (i < n-1):
                l[i][j] -= 4 
                l[i-1][j] +=1 
                l[i+1][j] += 1
                l[i][j-1] += 1
                l[i][j+1] += 1
            elif l[i][j]>= 4 and (j == 0) and (i == 0):
                l[i][j] -= 4 
                l[i+1][j] += 1
                l[i][j+1] += 1
            elif l[i][j]>= 4 and  j == n-1 and i == n-1:
                l[i][j] -= 2 
                l[i-1][j] +=1 
                l[i][j-1] += 1
            elif l[i][j]>= 4 and j == 0 and i > 0  and i < n-1:
                l[i][j] -= 4 
                l[i-1][j] +=1 
                l[i+1][j] += 1
                l[i][j+1] += 1
            elif l[i][j]>= 4 and j == 0 and i == n-1:
                l[i][j] -= 4 
                l[i-1][j] +=1 
                l[i][j+1] += 1
            elif l[i][j]>= 4 and i > 0 and j == n-1 and i < n-1:
                l[i][j] -= 4 
                l[i-1][j] +=1 
                l[i][j-1] += 1
                l[i+1][j] += 1
            elif l[i][j]>= 4 and j > 0 and j < n-1 and i == n-1:
                l[i][j] -= 4 
                l[i-1][j] +=1 
                l[i][j-1] += 1
                l[i][j+1] += 1
            elif l[i][j]>= 4 and j > 0 and i == 0 and j < n-1 :
                l[i][j] -= 4 
                l[i+1][j] += 1
                l[i][j-1] += 1
                l[i][j+1] += 1
            elif l[i][j]>= 4 and j == n-1 and i == 0:
                l[i][j] -= 4 
                l[i+1][j] +=1 
                l[i][j-1] += 1
    grillage(n,taille)
    #placement(n,taille)
    racine.after(500,lambda : ecoulement(n,taille))
                
                        
def configuration_geometrique(n):
    """cree une configuration ou la case du centre est surcharger a l'infini et ne fait que donner des grains"""
    global l 
    l = []
    for i in range(n):
        a = []
        for j in range(n):
            if i == n//2 and j == n//2:
                a.append(1300000)
            else:
                a.append(0) 
        l.append(list(a))


def copie():
    """copie la matrice d'une configuration dans un fichier text"""
    fic = open("sauvegarde.txt","w")
    fic.write(str(len(l)) + "\n" + "_____" )
    fic.close
    
    
#########################################
# programme principal
racine = tk.Tk()

canvas = tk.Canvas(racine,width= WIDTH, height= HEIGHT, bg= "black")
canvas.grid(column=1,row=0, rowspan= 20)


bouton = tk.Button(racine,text="configuration aléatoire",command=  lambda : construction_terrain(ligne,HEIGHT))
bouton.grid(column=0,row=0)

bouton1 = tk.Button(racine,text="ecoulement",command=  lambda : ecoulement(ligne,HEIGHT))
bouton1.grid(column=0,row=1)

bouton2 = tk.Button(racine, text="sauvegarder",command= copie)
bouton2.grid(column= 0, row= 2 )

racine.mainloop()
#########################@
# fin du code

