grille_morpion = {"A":["X","X","X"],"B":["X","X","X"],"C":["X","_","_"]}

while True:

    def afficher_grille():
        print('   1     2     3')
        for valeur, item in grille_morpion.items():
            print(valeur, item)


    def jouer_coup():
        joueur = 'X'
        colonne = int(input('choisir une colonne: 1, 2, 3 ?'))
        ligne = input('choisir ligne ? A, B, C')
        if verif_coup(ligne,colonne) == 1:
            grille_morpion[ligne][colonne -1] = joueur
            afficher_grille()
        


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
            return 1


    def est_pleine():
        case_rempli = 0
        for item in grille_morpion:
            for i in range(3):
                if grille_morpion[item][i] == "X":
                    case_rempli += 1
        if case_rempli == 9:
            print('grille rempli')
            return 1



    jouer_coup()
    est_pleine()       
    

