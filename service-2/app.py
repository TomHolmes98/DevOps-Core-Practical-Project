from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/get_name', methods=['GET'])
def get_name():
    first_name = ['Freddie', 'Jimmy', 'Kumar', 'Stuart', 'Ben', 'Sachin', 'Andrew', 'Chris', 'David', 'Steve']
    last_name = ['Flintoff', 'Anderson', 'Sangakarra', 'Broad', 'Stokes', 'Tendulkar', 'Strauss', 'Gayle', 'Smith']
    player_name = f"{random.choice(first_name)} {random.choice(last_name)}"
    return player_name

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
