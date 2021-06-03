from random import randrange
from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/get_score', methods=['POST'])
def get_score():
    name = request.json["name"]
    shot = request.json["shot"]
    score = 0
    if len(name)>5:
        score+=2
    if shot in ["Pull", "Hook", "Ramp", "Sweep"]:
        score+=4
    else:
        score+=1
    return jsonify(score)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)