grille_morpion = {"A":["X","_","_"],"B":["_","_","_"],"C":["_","_","_"]}

while True:

    def afficher_grille():
        print('   1     2     3')
        for valeur, item in grille_morpion.items():
            print(valeur, item)


    def jouer_coup():
        joueur = 'X'
        colonne = int(input('choisir une colonne: 1, 2, 3 ?'))
        ligne = input('choisir ligne ? A, B, C')
        grille_morpion[ligne][colonne -1] = joueur
        


    def verif_coup(ligne, colonne):
        if ligne not in ["A","B","C"]:
            print("out of range")
            return False
        if colonne not in [1,2,3]:
            print("out of range")
            return False
        if grille_morpion[ligne][colonne -1] != "_":
            print("case deja joué")
        else : 
            afficher_grille()




    verif_coup("A",2)
    break

    

