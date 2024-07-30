hauteur =6
largeur = 7

plateau = [['Ο' for _ in range(largeur)] for _ in range(hauteur)]

for h in range(hauteur):
    for l in range(largeur):
        print((plateau[h][l]), end = "    ")
    print("\n")

print("test sten")