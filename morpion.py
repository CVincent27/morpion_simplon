grille_morpion = {"A":["_","_","_"],"B":["_","_","_"],"C":["_","_","_"]}


def afficher_grille():
    print("   1   2   3")
    for ligne, valeurs in grille_morpion.items():
        print(f"{ligne}  {' | '.join(valeurs)}")


def jouer_coup(joueur):
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
                if grille_morpion[item][i] == "X" or grille_morpion[item][i] == "O":
                    case_rempli += 1
                
    if case_rempli == 9:
        print('grille rempli')
        return 1


def est_gagnante(joueur):
    for item in grille_morpion:
        if grille_morpion[item][0] == grille_morpion[item][1] == grille_morpion[item][2] == joueur:
            print(f"gagné ligne {item}")
            return 1
            
    for i in range(3):
        if grille_morpion['A'][i] == grille_morpion['B'][i] == grille_morpion['C'][i] == joueur:
            print(f'gagné colonne {i+1}')
        
    if grille_morpion['A'][0] == grille_morpion['B'][1] == grille_morpion['C'][2] == joueur:
        print('diagonale')
        
    if grille_morpion['A'][2] == grille_morpion['B'][1] == grille_morpion['C'][0] == joueur:
        print('diagonale')


while True:
    jouer_coup("X")
    if est_gagnante('X') == 1:
        break
    if est_pleine() == 1:
        break     
    jouer_coup("O")
    if est_gagnante('O') == 1:
        break
    if est_pleine() == 1:
        break     

