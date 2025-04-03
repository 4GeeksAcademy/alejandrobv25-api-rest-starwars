from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Modelo User
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    # Relación para los favoritos del usuario
    favorites = db.relationship('UserFavorite', back_populates='user', cascade="all, delete-orphan")
    def __repr__(self):
        return f'<User {self.username}>'
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
# Modelo Character
class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    race = db.Column(db.String(100), nullable=False)
    # Relación con UserFavorite
    favorites = db.relationship('UserFavorite', back_populates='character', cascade="all, delete-orphan")
    def __repr__(self):
        return f'<Character {self.name}>'
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "race": self.race

        }
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "race": self.race
        }
# Modelo Planet
class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    climate = db.Column(db.String(100), nullable=False)
    # Relación con UserFavorite
    favorites = db.relationship('UserFavorite', back_populates='planet', cascade="all, delete-orphan")
    def __repr__(self):
        return f'<Planet {self.name}>'
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate
        }
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate
        }
# Modelo UserFavorite
class UserFavorite(db.Model):
    __tablename__ = 'user_favorites'
    id = db.Column(db.Integer, primary_key=True)
    # Relación con User
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='favorites')
    # Relación con Character
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=True)  # Cambiado a nullable=True
    character = db.relationship('Character', back_populates='favorites')
    # Relación con Planet
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=True)  # Cambiado a nullable=True
    planet = db.relationship('Planet', back_populates='favorites')
    def __repr__(self):
        return f'<UserFavorite User {self.user_id}, Character {self.character_id}, Planet {self.planet_id}>'
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id
        }
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id
        }