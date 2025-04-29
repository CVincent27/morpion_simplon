grille_morpion = {"A":["_","_","_"],"B":["_","_","_"],"C":["_","_","_"]}

while True:

    def afficher_grille():
        print('   1     2     3')
        for valeur, item in grille_morpion.items():
            print(valeur, item)
        
        print(grille_morpion['A'][0])


    def jouer_coup():
        print('test')
        joueur = 'X'
        colonne = int(input('choisir une colonne: 1, 2, 3 ?'))
        ligne = input('choisir ligne ? A, B, C')
        grille_morpion[ligne][colonne -1] = joueur




    jouer_coup()
    afficher_grille()
    

