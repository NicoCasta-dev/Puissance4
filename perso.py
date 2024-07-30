ligne = 6
colonne = 7

tour = 0

def tableau_vide(ligne, colonne, colonne_actuelle, tour):

    for c in range(colonne):
        if c == colonne_actuelle:
            if tour % 2 == 0:
                print('🟡', end=' ')
            else:
                print('🔴', end=' ')
        else:
            print('  ', end=' ')
    print()

    for _ in range(ligne):
        for _ in range(colonne):
            print('⚫', end=' ')
        print()

colonne_actuelle = 0

# def valider_coup(ligne, colonne, colonne_actuelle, tour):

#     for c in range(colonne):
#         if tour % 2 == 0:
#             print('🟡', end=' ')
#         else:
#             print('🟡', -1)
            


while True:
    tableau_vide(ligne, colonne, colonne_actuelle, tour)
    
    mouvement = input("Où souhaitez-vous déplacer le jeton ? (Q / D) ").lower()

    if mouvement == 'q' and colonne_actuelle > 0:
        colonne_actuelle -= 1
        

    elif mouvement == 'd' and colonne_actuelle < colonne - 1:
        colonne_actuelle += 1

# while True :
# def valider_coup(ligne, colonne, colonne_actuelle, tour)
    
#     valider = input("Appuyez sur 's' pour valider votre coup ")

#     if valider == "s" :
