from flask import Flask, jsonify, request
from Librairie import Librairie

fnac = Librairie("fnac", "36 rue de la boustifaille")
fnac.ajouter_livre(["Harry Potter", "JK Rowling"])
fnac.ajouter_livre(["La guerre des mondes", "HG Wells"])
app = Flask(__name__)


@app.route("/test")
def hello_world():
    return "Ma page html est ici"


@app.route("/librairie")
def afficher_librairie():
    dictLibrairie = {}
    dictLibrairie["nom"] = fnac.get_nom()
    dictLibrairie["adresse"] = fnac.get_adresse()
    dictLibrairie["livres"] = {}
    for livre in fnac.get_livre():
        dictLibrairie["livres"][livre[0]] = livre[1]
    return dictLibrairie, 200


@app.route("/librairie/nom")
def afficher_nom():
    return jsonify(fnac.get_nom()), 200


@app.route("/librairie/adresse")
def afficher_adresse():
    return jsonify(fnac.get_adresse()), 200


@app.route("/librairie/livres")
def afficher_livres():
    dictLivres = {}
    for livre in fnac.get_livre():
        dictLivres[livre[0]] = livre[1]
    return dictLivres, 200


@app.route("/librairie/livres", methods=["POST"])
def ajouter_livre():
    livreRequest = request.get_json()
    if livreRequest.get("titre") == None:
        return "Error with the json, titre not found", 400
    if livreRequest.get("auteur") == None:
        return "Error with the json, auteur not found", 400
    print([])
    fnac.ajouter_livre([livreRequest["titre"], livreRequest["auteur"]])
    return "Book add with success", 204


@app.route("/librairie/livres", methods=["DELETE"])
def supprimer_livre():
    livreRequest = request.get_json()
    if livreRequest.get("titre") == None:
        return "Error with the json, titre not found", 400
    if livreRequest.get("auteur") == None:
        return "Error with the json, auteur not found", 400
    fnac.supprimer_livre([livreRequest["titre"], livreRequest["auteur"]])
    return "Book deleted with success", 204
