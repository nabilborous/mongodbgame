import os
from game import *
from utils import *
from db_init import *

def choix(choix):
    if (choix == 1):
        return True
    elif (choix == 3):
        return False

def jouer(chiffre):
    while True :
        chiffre = input("Que faire? : ")
        if chiffre.isdigit() and int(chiffre) > 0 and int(chiffre) < 4:
            chiffre = int(chiffre)
            if (chiffre != 2):
                return choix(chiffre)
            afficher_places()
        else:
            print("Reponse invalide, recommence.")

def afficher_menu_et_jouer():
    os.system('cls' if os.name == 'nt' else 'clear')
    titre = "Jeu de combat"
    afficher_header(titre)
    afficher_choix()
    return jouer(0)

def changer_score(premier_stats, deuxième_stats, troisième_stats, vagues, pseudonyme):
    scores = [("Score1", premier_stats), ("Score2", deuxième_stats), ("Score3", troisième_stats),]
    scores.sort(key=lambda x: x[1]["Score"], reverse=True)
    if vagues <= scores[-1][1]["Score"]:
        return
    scores[-1] = (scores[-1][0], {"Nom": pseudonyme, "Score": vagues})
    scores.sort(key=lambda x: x[1]["Score"], reverse=True)
    nouveau_score = { "Score1": scores[0][1], "Score2": scores[1][1], "Score3": scores[2][1] }
    ScoreCol.replace_one({"_id": ScoreCol.find_one()["_id"]}, nouveau_score)

def recup_classement(vagues):
    pseudonyme = input("Quel est ton pseudo? : ")
    doc = ScoreCol.find_one({}, {"_id": 0})
    list_classement = list(doc.items())
    _, premier_stats = list_classement[0]
    _, deuxième_stats = list_classement[1]
    _, troisième_stats = list_classement[2]
    changer_score(premier_stats, deuxième_stats, troisième_stats, vagues, pseudonyme)
    main()

def main():
    if afficher_menu_et_jouer() == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        (persos, persosStats) = creer_equipe()
        (ennemi, ennemiStats) = choix_ennemi()
        vagues = lancer_vagues(0, persos, persosStats, ennemi, ennemiStats)
        print(f"Tu as survécu {vagues} vagues.")
        recup_classement(vagues)
    else:
        print("You quit the game.")

main()