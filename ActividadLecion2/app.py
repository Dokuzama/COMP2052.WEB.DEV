from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Simple TODO API"

@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "nombre": "Proyecto Capstone",
        "version": "1.0",
        "autor": "Tu Nombre"
    })

@app.route("/mensaje", methods=["POST"])
def mensaje():
    data = request.get_json()
    mensaje_usuario = data.get("mensaje", "")
    respuesta = f"Recibí tu mensaje: {mensaje_usuario}"
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run(debug=True)
