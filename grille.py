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
    
    
    for h in range(hauteur-1, -1, -1):
        if plateau[h][col] == '🔘':
            plateau[h][col] = joueur
            break
    afficher_grille()


def jouer():
    while True:
        col = int(input("joueur 1, dans quelle colonne voulez-vous placer votre pion?"))
        placer_pion(col, joueur1)
        col = int(input("joueur 2, dans quelle colonne voulez-vous placer votre pion?"))
        placer_pion(col, joueur2)

afficher_grille()
jouer()
