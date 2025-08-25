from sqlalchemy import Column, ForeignKey, Integer, String, inspect
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.ext.hybrid import hybrid_property


class Base(DeclarativeBase):
    def to_dict(self):
        # dict_ = {}
        # for key in self.__mapper__.c.keys():
        #     if not key.startswith('_'):
        #         dict_[key] = getattr(self, key)

        # for key, prop in inspect(self.__class__).all_orm_descriptors.items():
        #     if isinstance(prop, hybrid_property):
        #         dict_[key] = getattr(self, key)
        # return dict_
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
    
    def to_dict(self):
        dct =  super().to_dict()
        dct["definitions"] = [df.to_dict() for df in self.definitions]
        return dct


class DefinitionMot(Base):
    __tablename__ = 'definition_mot'
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    mot_id = Column(Integer, ForeignKey('mot.id'))
    definition = Column(String)
    mot = relationship("Mot")

    def __repr__(self):
        return f"DefinitionMot(id={self.id}, definition=\"{self.definition}\")"
