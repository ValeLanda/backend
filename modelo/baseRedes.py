from sqlalchemy import Column, DateTime, ForeignKey, String, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Usuario(Base):
    __tablename__ = 'Usuario'
    __table_args__ = {'schema' : 'house'}

    idUsuario = Column(INTEGER(11), primary_key=True)
    nombreUsuario = Column(String(45), nullable =False)
    nombre = Column(String(45), nullable = False)
    apellidoP = Column(String(45), nullable=False)
    apellidoM = Column(String(45), nullable=True)
    contrasenia = Column(String(45), nullable=False)
    correo = Column(String(45), nullable=False)


class VideoJuego(Base):
    __tablename__ = 'VideoJuego'
    __table_args__ = {'schema' : 'house'}
    idVideoJuego = Column(INTEGER(11), primary_key=True)
    nombre = Column(String(45), nullable=False)
    genero = Column(String(45), nullable=True)
    descripcion = Column(String(45), nullable=True)
    clasificacion = Column(String(45), nullable=True)
    consola = Column(String(45), nullable=True)
    precio = Column(DOUBLE, nullable=False)
    
class Tener(Base):
    __tablename__ = 'Tener'
    __table_args__ = {'schema' : 'house'}

    idUsuario = Column(ForeignKey('house.Usuario.idUsuario'), nullable=False, index=True)
    idVideoJuego = Column(ForeignKey('house.VideoJuego.idVideoJuego'), nullable=False, index=True)

