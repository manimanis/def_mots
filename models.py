from sqlalchemy import ForeignKey
from database import db

class TypeMot(db.Model):
    __tablename__ = 'type_mots'
    id = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False,
        index=True
    )
    type_mot = db.Column(db.String)

    def __repr__(self):
        return f"TypeMot(id={self.id}, type_mot=\"{self.type_mot}\")"


class Mot(db.Model):
    __tablename__ = 'mots'
    id = db.Column(db.Integer, primary_key=True, nullable=False, index=True)
    mot = db.Column(db.String)
    type_mot_id = db.Column(db.Integer, ForeignKey('type_mots.id'))
    type_mot = db.relationship("TypeMot")

    def __repr__(self):
        return f"Mot(id={self.id}, mot=\"{self.mot}\")"

class DefinitionMot(db.Model):
    __tablename__ = 'definitions_mots'
    id = db.Column(db.Integer, primary_key=True, nullable=False, index=True)
    mot_id = db.Column(db.Integer, ForeignKey('mots.id'))
    definition = db.Column(db.String)

    def __repr__(self):
        return f"DefinitionMot(id={self.id}, definition=\"{self.definition}\")"
