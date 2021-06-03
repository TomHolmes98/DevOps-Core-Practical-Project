from flask import Flask, request, jsonify
import random

app = Flask(__name__)

shots = ["Pull", "Hook", "Ramp", "Sweep", "Drive", "Cut", "Switch Hit"]

@app.route('/get_shot', methods=['GET'])
def get_shot():
    return jsonify({"shot": random.choice(shots)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)