import os
import keyboard
import time
import sys

hauteur =6
largeur = 7
joueur1 ="❌"
joueur2= "💩"
curseur = "🔽    "
plateau = [['🔘' for _ in range(largeur)] for _ in range(hauteur)]
termine = False
ligneCurseur = ["      ","      ","      ","      ","      ","      ","      "]
ligneCurseur[0] = curseur

def afficher_grille():
    os.system('cls')
    for i in range(len(ligneCurseur)):
        print(ligneCurseur[i],end = "")
    print("")
    for h in range(hauteur):
        for l in range(largeur):
            print((plateau[h][l]), end = "    ")
        print("\n")



def placer_pion(l, joueur):
    os.system('cls')
    global termine
    
    for h in range(hauteur-1, -1, -1):
        if plateau[h][l] == '🔘':
            plateau[h][l] = joueur
            victoire()
            if termine :
                afficher_grille()
                sys.exit(0)
            break
    afficher_grille()
                


def victoire( ):
     global termine
     for h in range(hauteur):
         for l in range(largeur):
             if ((h<=2 and plateau[h][l] == joueur1) and (plateau[h+1][l] == plateau[h+2][l] == plateau[h+3][l] == joueur1)) or ((l<=3 and plateau[h][l] == joueur1 ) and (plateau[h][l+1] == plateau[h][l+2] == plateau[h][l+3] == joueur1)) or ((h<=2 and l<=3 and plateau[h][l] == joueur1) and (plateau[h+1][l+1] == plateau[h+2][l+2] == plateau[h+3][l+3] == joueur1)) or ((h<=2 and l>=3 and plateau[h][l] == joueur1) and (plateau[h+1][l-1] == plateau[h+2][l-2] == plateau[h+3][l-3] == joueur1)):
                 print("Puissance 4! La victoire revient au joueur 1!")
                 termine = True

             elif ((h<=2 and plateau[h][l] == joueur2) and (plateau[h+1][l] == plateau[h+2][l] == plateau[h+3][l] == joueur2)) or ((l<=3 and plateau[h][l] == joueur2 ) and (plateau[h][l+1] == plateau[h][l+2] == plateau[h][l+3] == joueur2)) or ((h<=2 and l<=3 and plateau[h][l] == joueur2) and (plateau[h+1][l+1] == plateau[h+2][l+2] == plateau[h+3][l+3] == joueur2)) or ((h<=2 and l>=3 and plateau[h][l] == joueur2) and (plateau[h+1][l-1] == plateau[h+2][l-2] == plateau[h+3][l-3] == joueur2)):
                 print("Puissance 4! La victoire revient au joueur 2!")
                 termine = True
    


def jouer():
    while termine == False:
        print("Tour joueur 1")
        col = deplacerCurseur(ligneCurseur, 1)
        placer_pion(col, joueur1)
        
        if termine == True:
            break
        col = deplacerCurseur(ligneCurseur,2)
        print(col)
   
 







        placer_pion(col, joueur2)
        
def deplacerCurseur(ligneCurseur, joueur):
    col = -1
    while True and col == -1:
       # print("Tour joueur 1" if jouer == 1 else "Tour joueur 2")
        indexCurseur = ligneCurseur.index(curseur)
        if keyboard.is_pressed("space"):
           col = indexCurseur
           time.sleep(0.3)
        if keyboard.is_pressed("left") and indexCurseur>0:
            ligneCurseur[indexCurseur]="      "
            ligneCurseur[indexCurseur-1]=curseur
            afficher_grille()
            time.sleep(0.3)
        elif keyboard.is_pressed("right") and indexCurseur<6:
            ligneCurseur[indexCurseur]="      "
            ligneCurseur[indexCurseur+1]=curseur
            afficher_grille()
            time.sleep(0.3)
    return col        
afficher_grille()

jouer()
