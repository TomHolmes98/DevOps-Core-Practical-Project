from flask import url_for
from flask_testing import TestCase
import requests_mock
from os import getenv

from app import app, db

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI=getenv('TEST_DATABASE_URI'),
            DEBUG=True,
            WTF_CSRF_ENABLED=False)
        return app
    
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestHome(TestBase):
    def test_home(self):
        name = {"name":"Freddie"}
        shot = {"shot":"Ramp"}

        with requests_mock.Mocker() as mocker:
            mocker.get('http://project_service_2:5000/get_name', json= name)
            mocker.get('http://project_service_3:5000/get_shot', json= shot)
            mocker.post('http://project_service_4:5000/get_score', text="6")
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Freddie scored 6 runs with a Ramp", response.data)