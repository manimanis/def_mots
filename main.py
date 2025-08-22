from contextlib import contextmanager
import os
import sys
from flask import Flask, jsonify, render_template, request
from database import SessionLocal, init_db
from models import DefinitionMot, Mot, TypeMot

cur_dir = os.path.dirname(__file__)

app = Flask(__name__)
init_db()

@app.route("/")
def index_page():
    return render_template("index.html")

@app.route('/mots', methods=['GET'])
def get_mots():
    session = SessionLocal()
    mots = [m.to_dict() for m in session.query(Mot).all()]
    session.close()
    return jsonify(mots)


# Créer un mot
@app.route('/mots', methods=['POST'])
def creer_utilisateur():
    data = request.get_json()
    print(data, file=sys.stderr)
    session = SessionLocal()
    type_mot = session.get(TypeMot, data['type_mot']['id'])
    mot = Mot(mot=data['mot'], type_mot=type_mot)
    definition = DefinitionMot(mot=mot, definition=data['definition'])
    session.add(mot)
    session.add(definition)
    session.commit()
    nouv_mot = mot.to_dict()
    session.close()
    return jsonify(nouv_mot), 201


@app.route('/types-mots', methods=['GET'])
def get_types_mots():
    session = SessionLocal()
    types_mots = [tm.to_dict() for tm in session.query(TypeMot).all()]
    if len(types_mots) == 0:
        types = ["Verbe", "Adverbe", "Adjectif", "Nom"]
        for typem in types:
            session.add(TypeMot(type_mot=typem))
        session.commit()
        types_mots = [tm.to_dict() for tm in session.query(TypeMot).all()]
    session.close()
    return jsonify(types_mots)


