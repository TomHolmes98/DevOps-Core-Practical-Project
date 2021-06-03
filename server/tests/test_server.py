from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_home():
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)