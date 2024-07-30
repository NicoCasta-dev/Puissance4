hauteur =6
largeur = 7
joueur1 ="❌"
joueur2= "💩"
plateau = [['🔘' for _ in range(largeur)] for _ in range(hauteur)]
termine = False

def afficher_grille():
    for h in range(hauteur):
        for l in range(largeur):
            print((plateau[h][l]), end = "    ")
        print("\n")



def placer_pion(col, joueur):
    
    
    for h in range(hauteur-1, -1, -1):
        if plateau[h][col] == '🔘':
            plateau[h][col] = joueur
            break
    afficher_grille()
                


def victoire():
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
        col = int(input("joueur 1, dans quelle colonne voulez-vous placer votre pion?"))
        placer_pion(col, joueur1)
        victoire()
        if termine == True:
        col = int(input("joueur 2, dans quelle colonne voulez-vous placer votre pion?"))
        placer_pion(col, joueur2)
        victoire()




afficher_grille()
jouer()
