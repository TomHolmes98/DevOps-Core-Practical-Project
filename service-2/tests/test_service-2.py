from flask import url_for
from flask_testing import TestCase
import requests_mock
from unittest.mock import patch

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestNameFreddie(TestBase):
    def test_get_Freddie(self):
        with patch('random.choice') as t:
            t.return_value = "Freddie"

            response = self.client.get(url_for('get_name'))
            self.assertIn(b"Freddie", response.data)



