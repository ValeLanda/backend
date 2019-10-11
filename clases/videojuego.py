
from backend.common.conexion import obtenerConexion
from backend.modelo.baseRedes import VideoJuego

def creaVideoJuego(dicc):
    s = obtenerConexion()
    vj = VideoJuego()
    vj.nombre = dicc['nombre']
    vj.genero = dicc['genero']
    vj.descripcion = dicc['descripcion']
    vj.clasificacion = dicc['clasificacion']
    vj.consola = dicc['consola']
    vj.precio = dicc['precio']
    s.add(vj)
    s.commit()

    