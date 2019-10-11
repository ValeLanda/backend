
from backend.common.conexion import obtenerConexion
from backend.modelo.baseRedes import Usuario

def verificaUsuario(nombreUsuario,contrasenia):
    s = obtenerConexion()
    us = s.query(Usuario).filter(Usuario.nombreUsuario==nombreUsuario, Usuario.contrasenia==contrasenia).first()
    if us!=None:
        usr = {"idUser": us.idUsuario}
        return usr

    else:
        return None

def creaUsuario(dicc):
    s = obtenerConexion
    usr = Usuario()
    usr.nombreUsuario = dicc['nombreUsuario']
    usr.nombre = dicc['nombre']
    usr.apellidoP = dicc['apellidoP']
    usr.apellidoM = dicc['apellidoM']
    usr.contrasenia = dicc['contrasenia']
    usr.correo = dicc['correo']
    s.add(usr)
    s.commit()


if __name__ == '__main__':
    main()




