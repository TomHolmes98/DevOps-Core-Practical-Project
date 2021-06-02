from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
import requests
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')

db = SQLAlchemy(app)

class Cricket(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    shot = db.Column(db.string(50), nullable = False)
    score = db.Column(db.Integer, nullable = False)

@app.route('/')
@app.route('/home')
def home():
    name = requests.get('http://service-2_api:5000/get_name')
    shot = requests.get('http://service-3_api:5000/get_shot')
    score = requests.post('http://service-4_api:5000/get_score')

    last_five = Cricket.query.order_by(Cricket.id.desc()).limit(5)

    db.session.add(
    Cricket(
        name = name.text,
        shot = shot.text,
        score = score.text
        )
    )
    db.session.commit()

    return render_template('index.html', title='Home', last_five=last_five)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)









