from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class TypeMot(Base):
    __tablename__ = 'type_mot'
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        index=True
    )
    type_mot = Column(String)

    def __repr__(self):
        return f"TypeMot(id={self.id}, type_mot=\"{self.type_mot}\")"


class Mot(Base):
    __tablename__ = 'mot'
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    type_mot_id = Column(Integer, ForeignKey('type_mot.id'))
    type_mot = relationship("TypeMot")
    mot = Column(String)
    definitions = relationship("DefinitionMot", backref="mots")

    def __repr__(self):
        return f"Mot(id={self.id}, mot=\"{self.mot}\", type_mot=\"{self.type_mot}\")"


class DefinitionMot(Base):
    __tablename__ = 'definition_mot'
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    mot_id = Column(Integer, ForeignKey('mot.id'))
    definition = Column(String)
    mot = relationship("Mot")

    def __repr__(self):
        return f"DefinitionMot(id={self.id}, definition=\"{self.definition}\")"
