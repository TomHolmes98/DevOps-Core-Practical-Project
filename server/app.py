from flask import Flask, render_template, json
from flask_sqlalchemy import SQLAlchemy 
import requests
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')

db = SQLAlchemy(app)

class Cricket(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    shot = db.Column(db.String(50), nullable = False)
    score = db.Column(db.Integer, nullable = False)

@app.route('/')
@app.route('/home')
def home():
    name = requests.get('http://project_service_2:5000/get_name')
    shot = requests.get('http://project_service_3:5000/get_shot')
    result = {**name.json(),**shot.json()}
    score = requests.post('http://project_service_4:5000/get_score',json=result)

    last_five = Cricket.query.order_by(Cricket.id.desc()).limit(5)

    db.session.add(
    Cricket(
        name = name.json()["name"],
        shot = shot.json()["shot"],
        score = score.json()
        )
    )
    db.session.commit()

    return render_template('index.html', name=name.json()["name"], shot=shot.json()["shot"], score=score.json(), last_five=last_five)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)









