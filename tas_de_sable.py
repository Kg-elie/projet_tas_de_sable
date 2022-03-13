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
import tkinter.messagebox as tkm

#########################################
# definitions des constantes            #
#########################################

HEIGHT = 600
WIDTH = 600

#########################################
#  definitions des variables            #
#########################################

# coisir une ligne qui ne fait pas de decimale si l'on divise la taille par elle
ligne =100
# matrice contenant les grain de sable pour chaque case
matrice = []
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

##########################################################################################################
# configuration
#####################################################

def configuration(n):
    """remplie la grille d'une configuration aléatoire"""
    global matrice 
    matrice = []
    for i in range(n):
        a = []
        for j in range(n):
            a.append(rd.randint(0,4))
        matrice.append(list(a))


def configuration_geometrique(n):
    """cree une configuration ou la case du centre a un nombre de grains donner par l'utilisateur"""
    global matrice, text
    if text.get() == '':
        alerte = tkm.showwarning("attention", "veuiller entrer un nombre de grains a mettre dans la case centrale")
        return
    
    matrice = []
    for i in range(n):
        a = []
        for j in range(n):
            if i == n//2 and j == n//2:
                a.append(int(text.get()))
            else:
                a.append(0) 
        matrice.append(list(a))


def config_creatif(n):
    """permet de creer une configuration nul"""
    global matrice 
    matrice = []
    for i in range(n):
        a = []
        for j in range(n):
            a.append(0) 
        matrice.append(list(a))


def config_stable(n):
    """permet de creer une configuration satble avec 4 grains par case"""
    global matrice 
    matrice = []
    for i in range(n):
        a = []
        for j in range(n):
            a.append(4) 
        matrice.append(list(a))


def config_indentity(n):
    """cree une matrice qui donnera si la taille est de 100/100 une configuration identity"""
    global matrice

    fic = open("identity.txt","r")
    ligne = fic.readline()
    N = int(ligne)
    a = []
    b= []
    matrice1 = []
    for i in fic:
        b.append(int(i))
        if len(b)==N:
            a.append(b)
            b = []
    matrice1 = list(a)
    matrice = []
    for i in range(n):
        a = []
        for j in range(n):
            a.append(8 - matrice1[i][j]) 
        matrice.append(list(a))
    

##########################################################################################################

##########################################################################################################
# construction des terrain 
#####################################################

def construction_terrain(n,taille):
    """ construire le terrain à partir de plusieus fonctions"""
    

    configuration(n)
    grillage(n,taille)
   

def construction_terrain_geometrique(n,taille):
    """ construire un terrain geometrique à partir de plusieus fonctions"""
    

    configuration_geometrique(n)
    grillage(n,taille)
   

def construction_terrain_nul(n,taille):
    """ construire un terrain nul à partir de plusieus fonctions"""
    

    config_creatif(n)
    grillage(n,taille)
   

def construction_terrain_stable(n,taille):
    """ construire un terrain stable à partir de plusieus fonctions"""
    config_stable(n)
    grillage(n,taille)


def construction_terrain_identity(n,taille):
    """ construire un terrain nul à partir de plusieus fonctions"""
    

    config_indentity(n)
    grillage(n,taille)

#########################################################################################################

def ecoulement(n,taille):
    """simule un ecoulement en donnant a chaque case voisine un grain de sable si la case est instable"""
    global case_id, matrice , interupteur
    arret = 0
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j]>= 4 and (j > 0) and (i > 0) and (j < n-1) and (i < n-1):
                matrice[i][j] -= 4 
                matrice[i-1][j] +=1 
                matrice[i+1][j] += 1
                matrice[i][j-1] += 1
                matrice[i][j+1] += 1
                arret = 1
            elif matrice[i][j]>= 4 and (j == 0) and (i == 0):
                matrice[i][j] -= 4 
                matrice[i+1][j] += 1
                matrice[i][j+1] += 1
                arret = 1
            elif matrice[i][j]>= 4 and  j == n-1 and i == n-1:
                matrice[i][j] -= 2 
                matrice[i-1][j] +=1 
                matrice[i][j-1] += 1
                arret = 1
            elif matrice[i][j]>= 4 and j == 0 and i > 0  and i < n-1:
                matrice[i][j] -= 4 
                matrice[i-1][j] +=1 
                matrice[i+1][j] += 1
                matrice[i][j+1] += 1
                arret = 1
            elif matrice[i][j]>= 4 and j == 0 and i == n-1:
                matrice[i][j] -= 4 
                matrice[i-1][j] +=1 
                matrice[i][j+1] += 1
                arret = 1
            elif matrice[i][j]>= 4 and i > 0 and j == n-1 and i < n-1:
                matrice[i][j] -= 4 
                matrice[i-1][j] +=1 
                matrice[i][j-1] += 1
                matrice[i+1][j] += 1
                arret = 1
            elif matrice[i][j]>= 4 and j > 0 and j < n-1 and i == n-1:
                matrice[i][j] -= 4 
                matrice[i-1][j] +=1 
                matrice[i][j-1] += 1
                matrice[i][j+1] += 1
                arret = 1
            elif matrice[i][j]>= 4 and j > 0 and i == 0 and j < n-1 :
                matrice[i][j] -= 4 
                matrice[i+1][j] += 1
                matrice[i][j-1] += 1
                matrice[i][j+1] += 1
                arret = 1
            elif matrice[i][j]>= 4 and j == n-1 and i == 0:
                matrice[i][j] -= 4 
                matrice[i+1][j] +=1 
                matrice[i][j-1] += 1
                arret = 1
    coloriage()
    if arret == 0:
        return
    if interupteur ==0 :
        racine.after(50,lambda : ecoulement(n,taille))
    if interupteur == 1:
        interupteur = 0

#########################################################################################################
# sauvegarde
#####################################################

def copie():
    """copie la matrice d'une configuration dans un fichier text"""
    global text
    if text.get() == '':
        alerte = tkm.showwarning("attention", "veuiller entrer un titre pour la sauvegarde")
        return
    if text.get() == 'identity':
        alerte = tkm.showwarning("attention", "ce nom de sauvegarde ne peut pas etre utilisée car neccessaire pour le fonctionnemnt du programme ")
        return
    titre = text.get() + ".txt"
    fic = open(titre,"w")
    fic.write(str(len(matrice)) + "\n"  )
    for i in matrice:
        for j in i:
            fic.write(str(j) + "\n")
    fic.close
    

def recuperation():
    """permet de recuperer une configuration sauvegarder et la generer"""
    global matrice, text
    if text.get() == '':
        alerte = tkm.showwarning("attention", "veuiller entrer le nom de la sauvegarde")
        return
    titre = text.get() + ".txt"
    fic = open(titre,"r")
    ligne = fic.readline()
    N = int(ligne)
    a = []
    b= []
    for i in fic:
        b.append(int(i))
        if len(b)==N:
            a.append(b)
            b = []
    matrice = list(a)
    grillage(N,HEIGHT)

#########################################################################################################


def stop():
    """permet de stopper l'ecoulement"""
    global interupteur

    if interupteur == 0:
        interupteur = 1
    elif interupteur == 1:
        interupteur = 0


def mode_player(event):
    """permet a l'utilisateur de donner des grains de sable lui-meme"""
    global matrice
    j =canvas.find_closest(event.x,event.y)
    c = (j[0]-1)// ligne 
    r = (j[0]-1) % ligne 
    while c > ligne or r > ligne:
        if c > ligne :
            c = c - ligne 
        if r > ligne:
            r = r - ligne
    
    matrice[c][r] +=1
    coloriage()
    

def coloriage():
    """permet d'attribuer une couleur a chaque case"""
    id = 0
    for i in matrice:
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

#########################################################################################################
# operation
#####################################################

def addition():
    """additione la matrice actuelle a elle meme"""
    global matrice , text
    if text.get() == '':
        alerte = tkm.showwarning("attention", "veuiller entrer le nom de la configuration a additioner")
        return
    titre = text.get() + ".txt"
    fic = open(titre,"r")
    ligne = fic.readline()
    N = int(ligne)
    a = []
    b= []
    matrice1 = []
    for i in fic:
        b.append(int(i))
        if len(b)==N:
            a.append(b)
            b = []
    matrice1 = list(a)

    for i in range (len(matrice)):
        for j in range (len(matrice)):
            matrice[i][j] = matrice[i][j] + matrice1[i][j]
    coloriage()


def soustraction():
    """soustrait la matrice actuelle a elle meme"""
    global matrice , text
    if text.get() == '':
        alerte = tkm.showwarning("attention", "veuiller entrer le nom de la configuration a soutraire")
        return
    titre = text.get() + ".txt"
    fic = open(titre,"r")
    ligne = fic.readline()
    N = int(ligne)
    a = []
    b= []
    matrice1 = []
    for i in fic:
        b.append(int(i))
        if len(b)==N:
            a.append(b)
            b = []
    matrice1 = list(a)

    for i in range (len(matrice)):
        for j in range (len(matrice)):
            matrice[i][j] = matrice[i][j] - matrice1[i][j]
            if matrice[i][j] < 0:
                matrice[i][j] = 0
    coloriage()


##########################################################################################################

#########################################
# programme principal                   #
#########################################

racine = tk.Tk()
racine.title("TAS DE SABLE")
canvas = tk.Canvas(racine,width= WIDTH, height= HEIGHT, bg= "black")
canvas.grid(column=3,row=0, rowspan= 20)

##########################################################################################################
# bouton creation de configuration
####################################################

boutonrandom = tk.Button(racine,text="configuration random",command=  lambda : construction_terrain(ligne,HEIGHT), activeforeground="green")
boutonrandom.grid(column=0,row=0)

bouton_pile = tk.Button(racine, text="config pile",command= lambda : construction_terrain_geometrique(ligne,HEIGHT), activeforeground="green")
bouton_pile.grid(column=1 , row= 0 )

bouton_creatif = tk.Button(racine, text="mode creatif",command= lambda : construction_terrain_nul(ligne,HEIGHT), activeforeground="green")
bouton_creatif.grid(column=2 , row= 0 )

bouton_stable = tk.Button(racine, text=" config max stable",command= lambda : construction_terrain_stable(ligne,HEIGHT), activeforeground="green")
bouton_stable.grid(column=0 , row= 1 )

bouton_identity = tk.Button(racine, text=" config identity",command= lambda : construction_terrain_identity(ligne,HEIGHT), activeforeground="green")
bouton_identity.grid(column=1 , row= 1 )

##########################################################################################################
# bouton fonctionalité
#####################################################

bouton_ecoulement = tk.Button(racine,text="ecoulement",command=  lambda : ecoulement(ligne,HEIGHT), activeforeground="green")
bouton_ecoulement.grid(column=0,row=2)

bouton_sauvegarde = tk.Button(racine, text="sauvegarder",command= copie, activeforeground="green")
bouton_sauvegarde.grid(column= 0, row= 3 )

bouton_charge = tk.Button(racine, text="charger",command= recuperation, activeforeground="green")
bouton_charge.grid(column= 1, row= 3 )

bouton_stop = tk.Button(racine, text="stop",command= stop, activeforeground="green")
bouton_stop.grid(column=1 , row= 2 , columnspan=1)

bouton_addition =  tk.Button(racine, text="Addition",command= addition, activeforeground="green")
bouton_addition.grid(column=0, row= 4)

bouton_soustraction =  tk.Button(racine, text="soustraction",command= soustraction, activeforeground="green")
bouton_soustraction.grid(column=1, row= 4)


##########################################################################################################
# barre de dialogue
#####################################################

text = tk.StringVar()
barre = tk.Entry(racine,textvariable= text, bd= 3, highlightcolor= "green")
barre.grid(column=2,row= 1 )
label_info = tk.Label(racine, text="FONCTIONS BARRE DE RECHERCHE : \n -choisir les nombres de grains \n pour la config pile \n - nommer la configuration a sauvegarder \n - chercher une sauvegarde avec son nom", bd= 3, relief="ridge")
label_info.grid(column=2,row=2)

##########################################################################################################

canvas.bind("<Button-1>",mode_player)
racine.mainloop()
##################################################
# fin du code

