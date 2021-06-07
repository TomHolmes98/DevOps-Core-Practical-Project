from flask import Flask, request, json, jsonify
import random

app = Flask(__name__)

name = ["Freddie", "Jimmy", "Kumar", "Stuart", "Ben", "Sachin", "Andrew", "Chris", "David", "Steve"]

@app.route('/get_name', methods=['GET'])
def get_name():
    #last_name = ['Flintoff', 'Anderson', 'Sangakarra', 'Broad', 'Stokes', 'Tendulkar', 'Strauss', 'Gayle', 'Smith']
    return jsonify({"name": random.choice(name)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
