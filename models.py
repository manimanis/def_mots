from sqlalchemy import ForeignKey
from database import db

class TypeMot(db.Model):
    id = db.Column(
        db.BigInteger,
        primary_key=True,
        nullable=False,
        index=True
    )
    type_mot = db.Column(db.String)


class Mot(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, nullable=False, index=True)
    mot = db.Column(db.String)
    type_mot_id = db.Column(db.BigInteger, ForeignKey('type_mot.id'))

class DefinitionMot(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, nullable=False, index=True)
    mot_id = db.Column(db.BigInteger, ForeignKey('mot.id'))
    definition = db.Column(db.String)
