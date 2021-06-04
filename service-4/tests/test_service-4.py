from flask import url_for, request
from flask_testing import TestCase
import requests_mock
from app import app 
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestScore(TestBase):
    def test_score(self):
        info = dict(name="Freddie", shot="Ramp")
        response = self.client.post(url_for('get_score'), json=info)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"6", response.data)





