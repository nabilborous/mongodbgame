from db_init import *
import random
import os
import time

def afficher_places():
    for player in list(ScoreCol.find()):
        print(f"Première place : {str(player["Score1"]["Nom"])} avec {str(player["Score1"]["Score"])}")
        print(f"Deuxième place : {str(player["Score2"]["Nom"])} avec {str(player["Score2"]["Score"])}")
        print(f"Troisième place : {str(player["Score3"]["Nom"])} avec {str(player["Score3"]["Score"])}")

def afficher_choix():
    print("1. Démarrer une nouvelle partie")
    print("2. Afficher les 3 meilleurs scores")
    print("3. Quitter\n")

def afficher_header(texte):
    print("-" * 50)
    print(texte.center(50))
    print("-" * 50)

def liste_persos():
    doc = CharacterCol.find_one({}, {"_id": 0})
    ListePersos = []
    ListeStats = []
    i = 0
    for nom_perso, stats in doc.items():
        print(f"Perso numéro {i}, Nom : {nom_perso}")
        i = i+1
        ListePersos.append(nom_perso)
        ListeStats.append(stats)
    return (ListePersos, ListeStats)

def choix_equipe(ListePersos, ListeStats):
    equipe = []
    equipeStats = []
    while len(equipe) < 3:
        num = input("Tu veux quel perso? Donne moi le chiffre : ")
        if num.isdigit() and int(num) < len(ListePersos):
            print(ListePersos[int(num)])
            equipe.append(ListePersos[int(num)])
            equipeStats.append(ListeStats[int(num)])
        else:
            print("Mauvaise valeur, entre un vrai numéro.")
    return (equipe, equipeStats)

def creer_equipe():
    print("Les personnages que tu peux selectionner sont : ")
    (ListePersos, ListeStats) = liste_persos()
    print("Il faut en choisir trois.")
    (equipe, equipe_stats) = choix_equipe(ListePersos, ListeStats)
    print(f"Votre equip est : {equipe}")
    time.sleep(2)
    return (equipe, equipe_stats)

def choix_ennemi():
    doc = MonsterCol.find_one({}, {"_id": 0})
    print(doc.items())
    print(list(doc.items()))
    randomEnnemi, stats = random.choice(list(doc.items()))
    print(f"L'ennemi est : {randomEnnemi}")
    print(stats)
    return (randomEnnemi, stats)

def affichage(equipe, equipeStats, ennemi, ennemiStats):
    print(f"Ennemi : {ennemi}\nVie : {ennemiStats["Vie"]}\nDéfense : {ennemiStats["Defense"]}\nAttaque : {ennemiStats["Attack"]}")
    print("-" * 50)
    print("Equipe : ")
    print(f"{equipe[0]} - Vie : {equipeStats[0]["Vie"]} - Défense : {equipeStats[0]["Defense"]} - Attaque : {equipeStats[0]["Attack"]}\n")
    print(f"{equipe[1]} - Vie : {equipeStats[1]["Vie"]} - Défense : {equipeStats[1]["Defense"]} - Attaque : {equipeStats[1]["Attack"]}\n")
    print(f"{equipe[2]} - Vie : {equipeStats[2]["Vie"]} - Défense : {equipeStats[2]["Defense"]} - Attaque : {equipeStats[2]["Attack"]}\n")