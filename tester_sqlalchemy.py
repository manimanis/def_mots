# types de mots
tm1 = TypeMot(type_mot="Verbe")
tm2 = TypeMot(type_mot="Adverbe")
tm3 = TypeMot(type_mot="Adjectif")
tm4 = TypeMot(type_mot="Nom")
db.session.add(tm1)
db.session.add(tm2)
db.session.add(tm3)
db.session.add(tm4)
db.session.commit()

# mots
mot1 = Mot(mot="Parler", type_mot=tm1)
mot2 = Mot(mot="Jouer", type_mot=tm1)
db.session.add(mot1)
db.session.add(mot2)
db.session.commit()
