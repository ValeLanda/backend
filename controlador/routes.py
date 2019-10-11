from backend.clases.usuario import verificaUsuario, creaUsuario
from flask import Flask, request, jsonify,make_response
app = Flask(__name__)


@app.route('/ruta')
def get_path():
    return ""

@app.route("/login",methods=['GET','POST'])
def login():
    data = request.json
    nombreUsuario = data['nombreUsuario']
    contrasenia = data['contrasenia']
    usr = verificaUsuario(nombreUsuario,contrasenia)
    if usr != None:
        return make_response(jsonify(usr), 200)

    else:
        return make_response(jsonify(message="no conectado"), 220)


@app.route("/creaUsuario", methods=['GET', 'POST'])
def creaUsuario():
    data = request.json
    dicc = {}
    dicc['nombreUsuario'] = data['nombreUsuario']
    dicc['nombre'] = data['nombre']
    dicc['apellidoP'] = data['apellidoP']
    dicc['apellidoM'] = data['apellidoM']
    dicc['contrasenia'] = data['contrasenia']
    dicc['correo'] = data['correo']
    creaUsuario(dicc)
    return make_response(jsonify(message="agregado"),200)



      
