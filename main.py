
def tableau_vide(ligne, colonne):
    print('  ' * colonne)


    for _ in range(ligne):
        for _ in range(colonne):
            print('⚫', end=' ')
        print() 



ligne = 6
colonne = 7

tableau_vide(ligne, colonne)
