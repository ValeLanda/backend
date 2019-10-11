from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import os

def obtenerConexion():
    host = 'localhost'
    user = 'dany'
    database = 'house'
    password = 'jonsnow13'

    connection = 'mysql+pymysql://'+ user+':'+password+'@'+host+':3306/'+database
    engine = sqlalchemy.create_engine(connection)
    connection = engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
    

