from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

class Aeronave(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'Aeronaves'
    aeronave_id = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.String(20), unique=True, nullable=False)
    modelo = db.Column(db.String(100), nullable=False)
    fabricante = db.Column(db.String(100))
    capacidad = db.Column(db.Integer)
    tipo_aeronave = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # Relación con vuelos
    vuelos = db.relationship('Vuelo', back_populates='aeronave')

class Piloto(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'Pilotos'
    piloto_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    licencia = db.Column(db.String(20), unique=True, nullable=False)
    horas_vuelo = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # Relaciones con vuelos
    vuelos_piloto = db.relationship('Vuelo', back_populates='piloto', foreign_keys='Vuelo.piloto_id')
    vuelos_copiloto = db.relationship('Vuelo', back_populates='copiloto', foreign_keys='Vuelo.copiloto_id')

class Vuelo(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'Vuelos'
    vuelo_id = db.Column(db.Integer, primary_key=True)
    numero_vuelo = db.Column(db.String(20), unique=True, nullable=False)
    origen = db.Column(db.String(100), nullable=False)
    destino = db.Column(db.String(100), nullable=False)
    fecha_salida = db.Column(db.DateTime, nullable=False)
    fecha_llegada = db.Column(db.DateTime, nullable=False)
    aeronave_id = db.Column(db.Integer, db.ForeignKey('Aeronaves.aeronave_id'), nullable=False)
    piloto_id = db.Column(db.Integer, db.ForeignKey('Pilotos.piloto_id'), nullable=False)
    copiloto_id = db.Column(db.Integer, db.ForeignKey('Pilotos.piloto_id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relaciones
    aeronave = db.relationship('Aeronave', back_populates='vuelos')
    piloto = db.relationship('Piloto', back_populates='vuelos_piloto', foreign_keys=[piloto_id])
    copiloto = db.relationship('Piloto', back_populates='vuelos_copiloto', foreign_keys=[copiloto_id])
    confirmaciones = db.relationship('Confirmacion', back_populates='vuelo')

class Confirmacion(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'Confirmaciones'
    confirmacion_id = db.Column(db.Integer, primary_key=True)
    vuelo_id = db.Column(db.Integer, db.ForeignKey('Vuelos.vuelo_id'), nullable=False)
    estado = db.Column(db.String(20), nullable=False)
    notas = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # Relación con vuelo
    vuelo = db.relationship('Vuelo', back_populates='confirmaciones')

class Usuario(db.Model, UserMixin):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'Usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    rol = db.Column(db.String(20), default='usuario')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class ConfiguracionAeropuerto(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'configuracion_aeropuerto'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, default='Mi Aeropuerto')
    codigo_iata = db.Column(db.String(3))
    codigo_icao = db.Column(db.String(4))
    director = db.Column(db.String(100))
    direccion = db.Column(db.String(200))
    codigo_postal = db.Column(db.String(10))
    municipio = db.Column(db.String(100))
    ciudad = db.Column(db.String(100))
    estado = db.Column(db.String(100))
    pais = db.Column(db.String(100), default='México')
    telefono = db.Column(db.String(20))
    email = db.Column(db.String(100))
    sitio_web = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
