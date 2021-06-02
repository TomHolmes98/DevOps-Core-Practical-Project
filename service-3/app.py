from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/get_shot', methods=['GET'])
def get_shot():
    shots = ['Pull', 'Hook', 'Ramp', 'Sweep', 'Drive', 'Cut', 'Switch Hit']
    return random.choice(shots)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)