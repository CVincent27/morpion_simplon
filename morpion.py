grille_morpion = {"A":["1","_","_"],"B":["_","_","_"],"C":["_","_","_"]}

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
        if verif_coup(colonne,ligne) == True:
            grille_morpion[ligne][colonne -1] = joueur
            afficher_grille()
        


    def verif_coup(colonne,ligne):
        if ligne not in ["A","B","C"]:
            print("out of range")
            return False
        if colonne not in [1,2,3]:
            print("out of range")
            return False
        else : 
            afficher_grille()




    jouer_coup()

    

