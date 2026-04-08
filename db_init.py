import pymongo
from models import *

# Création de la base de donnée
client = pymongo.MongoClient("mongodb://localhost:27017")
Database = client["Database"]
CharacterCol = Database["Personnages"]
MonsterCol = Database["Monstres"]
ScoreCol = Database["Scores"]

CharacterCol.drop()
MonsterCol.drop()

# Insertion dans la base de donnée
CharacterCol.insert_one(dictPersonnages)
MonsterCol.insert_one(dictMonstres)