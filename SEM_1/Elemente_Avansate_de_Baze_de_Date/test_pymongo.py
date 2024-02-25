import pymongo
from pymongo import MongoClient

conexiune = MongoClient("localhost", 27017)
db = conexiune.test

colectie = db.angajati

element = colectie.find_one()
print(element["nume"])
