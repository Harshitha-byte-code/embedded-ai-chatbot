from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "alive"})

@app.route("/move", methods=["POST"])
def move():
    data = request.get_json()
    direction = data.get("direction")
    speed = data.get("speed")

    print(f"[VEHICLE COMMAND RECEIVED] Direction: {direction}, Speed: {speed}")

    return jsonify({
        "status": "ok",
        "direction": direction,
        "speed": speed
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
