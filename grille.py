import os
import keyboard
import time

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



def placer_pion(col, joueur):
    global termine
    
    for h in range(hauteur-1, -1, -1):
        if plateau[h][col] == '🔘':
            plateau[h][col] = joueur
            
            if ((h<=2 and plateau[h][col] == joueur1) and (plateau[h+1][col] == plateau[h+2][col] == plateau[h+3][col] == joueur1)) or ((col<=3 and plateau[h][col] == joueur1 ) and (plateau[h][col+1] == plateau[h][col+2] == plateau[h][col+3] == joueur1)) or ((h<=2 and col<=3 and plateau[h][col] == joueur1) and (plateau[h+1][col+1] == plateau[h+2][col+2] == plateau[h+3][col+3] == joueur1)) or ((h<=2 and col>=3 and plateau[h][col] == joueur1) and (plateau[h+1][col-1] == plateau[h+2][col-2] == plateau[h+3][col-3] == joueur1)):
                print("Puissance 4! La victoire revient au joueur 1!")
                termine = True

            elif ((h<=2 and plateau[h][col] == joueur2) and (plateau[h+1][col] == plateau[h+2][col] == plateau[h+3][col] == joueur2)) or ((col<=3 and plateau[h][col] == joueur2 ) and (plateau[h][col+1] == plateau[h][col+2] == plateau[h][col+3] == joueur2)) or ((h<=2 and col<=3 and plateau[h][col] == joueur2) and (plateau[h+1][col+1] == plateau[h+2][col+2] == plateau[h+3][col+3] == joueur2)) or ((h<=2 and col>=3 and plateau[h][col] == joueur2) and (plateau[h+1][col-1] == plateau[h+2][col-2] == plateau[h+3][col-3] == joueur2)):
            
                print("Puissance 4! La victoire revient au joueur 2!")
                termine = True
            break
    os.system('cls')
    afficher_grille()
                


# def victoire():
#     global termine
#     for h in range(hauteur):
#         for l in range(largeur):
#             if ((h<=2 and plateau[h][l] == joueur1) and (plateau[h+1][l] == plateau[h+2][l] == plateau[h+3][l] == joueur1)) or ((l<=3 and plateau[h][l] == joueur1 ) and (plateau[h][l+1] == plateau[h][l+2] == plateau[h][l+3] == joueur1)) or ((h<=2 and l<=3 and plateau[h][l] == joueur1) and (plateau[h+1][l+1] == plateau[h+2][l+2] == plateau[h+3][l+3] == joueur1)) or ((h<=2 and l>=3 and plateau[h][l] == joueur1) and (plateau[h+1][l-1] == plateau[h+2][l-2] == plateau[h+3][l-3] == joueur1)):
#                 print("Puissance 4! La victoire revient au joueur 1!")
#                 termine = True

#             elif ((h<=2 and plateau[h][l] == joueur2) and (plateau[h+1][l] == plateau[h+2][l] == plateau[h+3][l] == joueur2)) or ((l<=3 and plateau[h][l] == joueur2 ) and (plateau[h][l+1] == plateau[h][l+2] == plateau[h][l+3] == joueur2)) or ((h<=2 and l<=3 and plateau[h][l] == joueur2) and (plateau[h+1][l+1] == plateau[h+2][l+2] == plateau[h+3][l+3] == joueur2)) or ((h<=2 and l>=3 and plateau[h][l] == joueur2) and (plateau[h+1][l-1] == plateau[h+2][l-2] == plateau[h+3][l-3] == joueur2)):
#                 print("Puissance 4! La victoire revient au joueur 2!")
#                 termine = True
    


def jouer():
    while termine == False:
        print("Tour joueur 1")
        col = deplacerCurseur(ligneCurseur)
        placer_pion(col, joueur1)
        
        if termine == True:
            break
        print("Tout joueur 2")
        col = deplacerCurseur(ligneCurseur)
        placer_pion(col, joueur2)
        
def deplacerCurseur(ligneCurseur):
    col = -1
    while True and col == -1:
        indexCurseur = ligneCurseur.index(curseur)
        if keyboard.is_pressed("enter"):
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
deplacerCurseur(ligneCurseur)

jouer()
