from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/get_score', methods=['POST'])
def get_score():
    score = str(len(request.data.decode('utf-8')))
    score_amount = ['1','2','3','4','5','6']
    return f"{score} scored {random.choice(score_amount)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)