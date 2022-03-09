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
ligne =60
# matrice contenant les grain de sable pour chaque case
l = []
# liste contenant les identifiants de chaque case
case_id = []
# permet de stopper l'ecoulement avec un systeme binaire(0;1)
interupteur = 0

 
#########################################
# definitions des fonctions             #
#########################################
def grillage(n,taille):
    """ cree une grille de n^2 case, et donne a chaque case une couleur selectionner en fonction du grain de sable qu'elle contient """
    global case_id
    
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
            case_id.append(canvas.create_oval((x,y),(x+rythme,y+rythme), fill="black" ,outline="black", width= 2 ))
            x += rythme
        y += rythme
    
    coloriage()


def configuration(n):
    """remplie la grille d'une configuration aléatoire"""
    global l 
    l = []
    for i in range(n):
        a = []
        for j in range(n):
            a.append(rd.randint(0,4))
        l.append(list(a))

          

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
    #placement(n,taille)



def construction_terrain_geometrique(n,taille):
    """ construire un terrain geometrique à partir de plusieus fonctions"""
    

    configuration_geometrique(n)
    grillage(n,taille)
    #placement(n,taille)


def construction_terrain_nul(n,taille):
    """ construire un terrain nul à partir de plusieus fonctions"""
    

    config_creatif(n)
    grillage(n,taille)
    #placement(n,taille)

    
def ecoulement(n,taille):
    """simule un ecoulement en donnant a chaque case voisine un grain de sable si la case est surchargée"""
    global case_id, l , interupteur

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
    coloriage()
    if interupteur ==0 :
        racine.after(50,lambda : ecoulement(n,taille))
    if interupteur == 1:
        interupteur = 0

                                     
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
    fic.write(str(len(l)) + "\n"  )
    for i in l:
        for j in i:
            fic.write(str(j) + "\n")
    fic.close
    

def recuperation():
    """permet de recuperer une configuration sauvegarder et la generer"""
    global l
    fic = open("sauvegarde.txt","r")
    ligne = fic.readline()
    N = int(ligne)
    a = []
    b= []
    for i in fic:
        b.append(int(i))
        if len(b)==N:
            a.append(b)
            b = []
    l = list(a)
    grillage(N,HEIGHT)
    #placement(N,HEIGHT)
    


def stop():
    """permet de stopper l'ecoulement"""
    global interupteur

    if interupteur == 0:
        interupteur = 1
    elif interupteur == 1:
        interupteur = 0

def mode_player(event):
    """permet a l'utilisateur dedonner des grains de sable lui-meme"""
    global l
    j =canvas.find_closest(event.x,event.y)
    c = (j[0]-1)// ligne 
    r = (j[0]-1) % ligne 
    while c > ligne or r > ligne:
        if c > ligne :
            c = c - ligne 
        if r > ligne:
            r = r - ligne
    
    l[c][r] +=1
    coloriage()
    

def coloriage():
    """permet d'attribuer une couleur a chaque case"""
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


def config_creatif(n):
    """permet de creer une configuration nul"""
    global l 
    l = []
    for i in range(n):
        a = []
        for j in range(n):
            a.append(0) 
        l.append(list(a))

#########################################
# programme principal
racine = tk.Tk()

canvas = tk.Canvas(racine,width= WIDTH, height= HEIGHT, bg= "black")
canvas.grid(column=3,row=0, rowspan= 20)


bouton = tk.Button(racine,text="configuration aléatoire",command=  lambda : construction_terrain(ligne,HEIGHT))
bouton.grid(column=0,row=0)

bouton1 = tk.Button(racine,text="ecoulement",command=  lambda : ecoulement(ligne,HEIGHT))
bouton1.grid(column=0,row=1)

bouton2 = tk.Button(racine, text="sauvegarder",command= copie)
bouton2.grid(column= 0, row= 2 )

bouton3 = tk.Button(racine, text="charger",command= recuperation)
bouton3.grid(column= 1, row= 2 )

bouton4 = tk.Button(racine, text="stop",command= stop)
bouton4.grid(column=1 , row= 1 , columnspan=1)

bouton5 = tk.Button(racine, text="config geometrique",command= lambda : construction_terrain_geometrique(ligne,HEIGHT))
bouton5.grid(column=1 , row= 0 )

bouton6 = tk.Button(racine, text="mode creatif",command= lambda : construction_terrain_nul(ligne,HEIGHT))
bouton6.grid(column=2 , row= 0 )

canvas.bind("<Button-1>",mode_player)
racine.mainloop()
#########################@
# fin du code

