from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    contraseña = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    genero = db.Column(db.String(80), nullable=False)
   

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "genero": self.genero
        }

class Personajes(db.Model):
    __tablename__ = "personajes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    fecha_nacimiento = db.Column(db.String(180))
    estatura= db.Column(db.String(180))
    genero = db.Column(db.String(200))
    favorito= db.relationship("Favoritos")

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "fecha_nacimiento": self.fecha_nacimiento,
            "estatura": self.estatura,
            "genero": self.genero
        }


class Planetas(db.Model):
    __tablename__ = "planetas"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    poblacion = db.Column(db.Integer)
    diametro= db.Column(db.Integer)
    gravedad = db.Column(db.String(200))
    favorito= db.relationship("Favoritos")

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "poblacion": self.poblacion,
            "diametro": self.diametro,
            "gravedad": self.gravedad
        }


class Favoritos(db.Model):
    __tablename__ = "favoritos"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    personajes_name = db.Column(db.String(200), db.ForeignKey("personajes.name"))
    planetas_name = db.Column(db.String(200), db.ForeignKey("planetas.name"))
    usuario_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "personajes_name": self.personajes_name,
            "planetas_name": self.planetas_name,
            "usuario_id": self.usuario_id,
        }


    
  
  
  