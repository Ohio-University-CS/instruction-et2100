
from flask import Flask, request, jsonify

app = Flask(__name__)

value = 10

@app.route("/value", methods=["GET"])
def get_value():
    return jsonify({"value": value})

@app.route("/value", methods=["POST"])
def set_value():
    global value
    value = request.json["value"]
    return jsonify({"value": value})

if __name__ == "__main__":
    app.run(port=5000)
