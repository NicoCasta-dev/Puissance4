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
    for i in range(5, 0, -1):
        if grille[i][col] == 0:
            grille[i][col] = joueur


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

placementDansGrille(6,2,plateau)
afficherGrille(plateau)
