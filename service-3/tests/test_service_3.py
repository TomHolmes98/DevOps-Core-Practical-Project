from flask import url_for, request
from flask_testing import TestCase
import requests_mock
from app import app 
from unittest.mock import patch 

class TestBase(TestCase):
    def create_app(self):
        return app

class TestShotRamp(TestBase):
    def test_get_Ramp(self):
        with patch('random.choice')as t:
            t.return_value = "Ramp"
            response = self.client.get(url_for('get_shot'))
            self.assertIn(b"Ramp", response.data)
