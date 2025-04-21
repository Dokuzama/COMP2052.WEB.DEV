from flask import Flask, request, jsonify

app = Flask (__name__)

@app.route("/", methods=["GET"])
def home():
    return "Simple TODO API"

@app.route("/todos", methods=["GET"])
def get_todos():
    return "List of TODOs"


if __name__ == "__main__":
    app.run(debug=True)

