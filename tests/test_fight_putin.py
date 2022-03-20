import unittest
import sys
import os
import json
from flask import Flask
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "elonmusk"))

from tests.mock_dialogflow_utils import *

from elonmusk.main import cloud_function

class TestFightPutin(unittest.TestCase):

    def test_do_to_putin(self):
        """Test that question about Putin has Putin in answer"""
        app = Flask(__name__)

        with app.app_context():
            putin_request = get_test_request("do_to_putin")
        
    
    def test_view_on_russia(self):
        """Test that question about Russia has Russia in answer"""
        app = Flask(__name__)

        with app.app_context():
            russia_request = get_test_request("view_on_russia")
    
    def test_concerns_about_kremlin(self):
        """Test that question about Kremlin has Kremlin in answer"""
        app = Flask(__name__)

        with app.app_context():
            kremlin_request = get_test_request("concerns_kremlin")

if __name__ == "__main__":
    unittest.main()