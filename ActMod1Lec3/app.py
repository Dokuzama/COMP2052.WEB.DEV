from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []

@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "sistema": "Gestión de Usuarios y Productos",
        "version": "1.0",
        "autor": "Tu Nombre"
    })

@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    data = request.get_json()

    nombre = data.get("nombre")
    correo = data.get("correo")

    if not nombre or not correo:
        return jsonify({"error": "Nombre y correo son obligatorios."}), 400

    nuevo_usuario = {"nombre": nombre, "correo": correo}
    usuarios.append(nuevo_usuario)

    return jsonify({"mensaje": "Usuario creado exitosamente.", "usuario": nuevo_usuario}), 201

@app.route("/usuarios", methods=["GET"])
def obtener_usuarios():
    return jsonify({"usuarios": usuarios})

if __name__ == "__main__":
    app.run(debug=True)

app = Flask (__name__)

@app.route("/", methods=["GET"])
def home():
    return "Simple TODO API"

@app.route("/todos", methods=["GET"])
def get_todos():
    return "List of TODOs"


if __name__ == "__main__":
    app.run(debug=True)
