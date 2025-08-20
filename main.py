from contextlib import contextmanager
import os
from flask import Flask, jsonify, render_template
import sqlite3

def connect_db():
    cur_dir = os.path.dirname(__file__)
    db = sqlite3.connect(os.path.join(cur_dir, 'dictionnaire.db3'))
    db.row_factory = sqlite3.Row
    return db

@contextmanager
def create_cursor(db: sqlite3.Connection):
    cur = db.cursor()
    yield cur
    cur.close()


app = Flask(__name__)

@app.route("/")
def index_page():
    return render_template("index.html")

@app.route("/words")
def list_words():
    db = connect_db()
    with create_cursor(db) as cur:
        cur.execute("SELECT * " +
                    "FROM mots AS m " +
                    "  INNER JOIN type_mots AS tm ON m.type = tm.numTypeMot " +
                    "ORDER BY mot")
        mots = cur.fetchall()
    return jsonify(mots)