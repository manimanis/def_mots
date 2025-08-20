from contextlib import contextmanager
import os
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from database import init_db
from models import TypeMot, db

@contextmanager
def create_cursor(db: sqlite3.Connection):
    cur = db.cursor()
    yield cur
    cur.close()

cur_dir = os.path.dirname(__file__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dictionnaire.db3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
init_db(app)

@app.route("/")
def index_page():
    return render_template("index.html")

@app.route("/words")
def list_words():
    type_mots = db.session.execute(db.select(TypeMot).order_by(TypeMot.type_mot)).fetchall()
    return jsonify(type_mots)