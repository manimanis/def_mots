from contextlib import contextmanager
import os
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from database import SessionLocal, init_db
from models import Mot, TypeMot

cur_dir = os.path.dirname(__file__)

app = Flask(__name__)
init_db()

@app.route("/")
def index_page():
    return render_template("index.html")

@app.route('/mots', methods=['GET'])
def get_mots():
    session = SessionLocal()
    mots = session.query(Mot).all()
    session.close()
    return jsonify(mots)

