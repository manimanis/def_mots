from database import SessionLocal, init_db
from sqlalchemy.orm import joinedload
from models import DefinitionMot, Mot, TypeMot

session = SessionLocal()
mots = session.query(Mot).options(joinedload(Mot.definitions)).all()
