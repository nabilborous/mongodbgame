import pymongo
from models import *
client = pymongo.MongoClient("mongodb://localhost:27017")
Database = client["Database"]
CharacterCol = Database["Personnages"]
MonsterCol = Database["Monstres"]
ScoreCol = Database["Scores"]

if __name__ == 'main':
    # Création de la base de donnée
    CharacterCol.drop()
    MonsterCol.drop()
    
    # Insertion dans la base de donnée
    CharacterCol.insert_one(dictPersonnages)
    MonsterCol.insert_one(dictMonstres)