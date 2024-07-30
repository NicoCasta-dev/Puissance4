ligne = 6
colonne = 7
joueur1 = '🟡'
joueur2 = '🔴'

plateau = [['⚫' for _ in range(colonne)] for _ in range(ligne)]

def afficher_grille():
    for h in range(ligne):
        for l in range(colonne):
            print(plateau[h][l], end=' ')
        print()

def valider_coup(colonne_actuelle, joueur):

    for h in range(ligne - 1, -1, -1):
        if plateau[h][colonne_actuelle] == '⚫':
            plateau[h][colonne_actuelle] = joueur
            return True
    return False

def jouer():
    tour = 0
    while True:
        afficher_grille()
        
        joueur_actuel = joueur1 if tour % 2 == 0 else joueur2
        
        mouvement = input(f"Joueur {'1' if joueur_actuel == joueur1 else '2'}, où souhaitez-vous déplacer le jeton ? (Q / D) ").lower()
        
        if mouvement == 'q' and colonne_actuelle > 0:
            colonne_actuelle -= 1
        elif mouvement == 'd' and colonne_actuelle < colonne - 1:
            colonne_actuelle += 1
        
        if valider_coup(colonne_actuelle, joueur_actuel):
            tour += 1
        else:
            print("Colonne pleine ou invalide, réessayez.")

colonne_actuelle = 0

jouer()


