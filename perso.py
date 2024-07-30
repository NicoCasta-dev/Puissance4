ligne = 6
colonne = 7
joueur1 = '🟡'
joueur2 = '🔴'

plateau = [['⚫' for _ in range(colonne)] for _ in range(ligne)]

colonne_actuelle = 0
tour = 0

def afficher_grille():

    for c in range(colonne):
        if c == colonne_actuelle:
            print(f'{joueur1 if tour % 2 == 0 else joueur2}', end='  ')
        else:
            print('  ', end=' ')
    print()
    

    for h in range(ligne):
        for l in range(colonne):
            print(plateau[h][l], end=' ')
        print()
    
    print()  


def valider_coup(colonne_actuelle, joueur):

    for h in range(ligne - 1, -1, -1):
        if plateau[h][colonne_actuelle] == '⚫':
            plateau[h][colonne_actuelle] = joueur
            return True
    return False


def victoire():
    global termine
    for h in range(ligne):
        for l in range(colonne):
            if ((h<=2 and plateau[h][l] == joueur1) and (plateau[h+1][l] == plateau[h+2][l] == plateau[h+3][l] == joueur1)) or ((l<=3 and plateau[h][l] == joueur1 ) and (plateau[h][l+1] == plateau[h][l+2] == plateau[h][l+3] == joueur1)) or ((h<=2 and l<=3 and plateau[h][l] == joueur1) and (plateau[h+1][l+1] == plateau[h+2][l+2] == plateau[h+3][l+3] == joueur1)) or ((h<=2 and l>=3 and plateau[h][l] == joueur1) and (plateau[h+1][l-1] == plateau[h+2][l-2] == plateau[h+3][l-3] == joueur1)):
                print("*** Puissance 4! La victoire revient au joueur 1 ! *** ")
                termine = True

            elif ((h<=2 and plateau[h][l] == joueur2) and (plateau[h+1][l] == plateau[h+2][l] == plateau[h+3][l] == joueur2)) or ((l<=3 and plateau[h][l] == joueur2 ) and (plateau[h][l+1] == plateau[h][l+2] == plateau[h][l+3] == joueur2)) or ((h<=2 and l<=3 and plateau[h][l] == joueur2) and (plateau[h+1][l+1] == plateau[h+2][l+2] == plateau[h+3][l+3] == joueur2)) or ((h<=2 and l>=3 and plateau[h][l] == joueur2) and (plateau[h+1][l-1] == plateau[h+2][l-2] == plateau[h+3][l-3] == joueur2)):
                print("*** Puissance 4! La victoire revient au joueur 2 ! ***")
                termine = True

run = True
while run:
    afficher_grille()
    

    mouvement = input("Où souhaitez-vous déplacer le jeton ? (Q / D pour déplacer, Enter pour placer) ").lower()
    
    if mouvement == 'q' and colonne_actuelle > 0:
        colonne_actuelle -= 1
    elif mouvement == 'd' and colonne_actuelle < colonne - 1:
        colonne_actuelle += 1
    elif mouvement == '':
        if valider_coup(colonne_actuelle, joueur1 if tour % 2 == 0 else joueur2):
            tour += 1
            victoire()
        else:
            print("Colonne pleine !")

    if victoire() == True:
        print("*** Partie terminé ! *** ")