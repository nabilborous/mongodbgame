from utils import *
import random
import time

wait = 0.5

def affichage_initial(persos, persos_stats, ennemi, ennemi_stats):
    print("Début de la partie! Voici ton équipe : ")
    affichage(persos, persos_stats, ennemi, ennemi_stats)
    time.sleep(2)

def lancer_vague_ennemi(persos, persos_stats, ennemi, ennemi_stats):
    persos_stats = vague_ennemi(persos, persos_stats, ennemi, ennemi_stats)
    affichage(persos, persos_stats, ennemi, ennemi_stats)
    time.sleep(wait)
    return persos_stats

def lancer_vague_persos(vagues, persos, persos_stats, ennemi, ennemi_stats):
    ennemi_stats = vague_persos(persos, persos_stats, ennemi, ennemi_stats)
    if ennemi_stats["Vie"] == 0:
        (ennemi, ennemi_stats) = nouvel_ennemi(ennemi)
        vagues = vagues + 1
    return (vagues, ennemi, ennemi_stats)

def lancer_vagues(vagues, persos, persos_stats, ennemi, ennemi_stats):
    affichage_initial(persos, persos_stats, ennemi, ennemi_stats)
    while True:
        persos_stats = lancer_vague_ennemi(persos, persos_stats, ennemi, ennemi_stats)
        if persos_stats[0]["Vie"] != 0 or persos_stats[1]["Vie"] != 0 or persos_stats[2]["Vie"] != 0:
            (vagues, ennemi, ennemi_stats) = lancer_vague_persos(vagues, persos, persos_stats, ennemi, ennemi_stats)
        else:
            print("Tout les personnages sont morts, fin de la run.")
            return vagues
            
def nouvel_ennemi(ennemi):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{ennemi} est vaincu !")
    (nouv_ennemi, nouv_ennemi_stats) = choix_ennemi()
    print(f"{nouv_ennemi} est apparu, un nouveau combat commence.")
    time.sleep(wait)
    return(nouv_ennemi, nouv_ennemi_stats)

def attack_perso(deg, perso_choisi, ennemi_choisi, ennemi_stats_choisi):
    print(f"{perso_choisi} attaque {ennemi_choisi} pour {deg} dégats.")
    ennemi_stats_choisi["Vie"] = ennemi_stats_choisi["Vie"] - deg
    if (ennemi_stats_choisi["Vie"] < 0):
        ennemi_stats_choisi["Vie"] = 0
    return ennemi_stats_choisi

def vague(perso_choisi, persos_stats_choisi, ennemi_choisi, ennemi_stats_choisi):
    deg = persos_stats_choisi["Attack"] - (ennemi_stats_choisi["Defense"] // 2)
    if (deg < 0):
        deg = 0
    return attack_perso(deg, perso_choisi, ennemi_choisi, ennemi_stats_choisi)

def vague_ennemi(persos, persos_stats, ennemi, ennemi_stats):
    os.system('cls' if os.name == 'nt' else 'clear')
    num = random.randint(0, 2)
    while (persos_stats[num]["Vie"] <= 0):
        num = random.randint(0, 2)
    persos_stats[num] = vague(ennemi, ennemi_stats, persos[num], persos_stats[num])
    return persos_stats

def vague_persos(persos, persos_stats, ennemi, ennemi_stats):
    i = 0
    for i in range(0, 3):
        if (persos_stats[i]["Vie"] > 0):
            os.system('cls' if os.name == 'nt' else 'clear')
            ennemi_stats = vague(persos[i], persos_stats[i], ennemi, ennemi_stats)
            affichage(persos, persos_stats, ennemi, ennemi_stats)
            time.sleep(wait)
    return ennemi_stats