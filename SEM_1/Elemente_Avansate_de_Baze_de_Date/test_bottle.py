import bottle
import pymongo


@bottle.route("/")
def index():
    conexiune = pymongo.MongoClient("localhost", 27017)
    db = conexiune.test

    colectie = db.angajati
    element = colectie.find_one()

    return "<center><b>Salut, %s!</br>" % element["nume"]


bottle.run(host="localhost", port=8080)
