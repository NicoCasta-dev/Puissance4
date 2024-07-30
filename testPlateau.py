import os

#grille[colonne][ligne]
# joueur 1 = ❌ & joueur 2 = 💩
def afficherGrille (grille):
    for i in range(6):
        for j in range(5):
            if(grille[i][j] == 1):
                print("❌", end="    ")
            elif(grille[i][j] == 2):
                print("💩",end="    ")
            else:
                print("🔘",end="    ")
        print("")

def placementDansGrille(col, joueur, grille):
    for i in range(6):
        if grille[col][i] == 0:
            grille[col][i] = joueur


os.system('cls')

plateau = [
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [2,2,2,2,2,2,2],
]

plateau[0][0]= 1
afficherGrille(plateau)
placementDansGrille(6,2,plateau)
afficherGrille(plateau)
