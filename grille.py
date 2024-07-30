hauteur =6
largeur = 7
joueur1 ="❌"
joueur2= "💩"
plateau = [['🔘' for _ in range(largeur)] for _ in range(hauteur)]

def afficher_grille():
    for h in range(hauteur):
        for l in range(largeur):
            print((plateau[h][l]), end = "    ")
        print("\n")



def placer_pion(col, joueur):
    
    
    for h in range(hauteur):
        for l in range(largeur):
            if plateau[h][col] == '🔘' and ((plateau[h-1][col] != '🔘') or h == 5):
                plateau[h][col] = joueur
                

            print((plateau[h][l]), end = "    ")
        print("\n")


placer_pion(3, joueur1)