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

            response = cloud_function(putin_request)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "Putin" in result["fulfillmentMessages"][0]["text"]["text"][0]
            )
        
    
    def test_view_on_russia(self):
        """Test that question about Russia has Russia in answer"""
        app = Flask(__name__)

        with app.app_context():
            russia_request = get_test_request("view_on_russia")

            response = cloud_function(russia_request)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "Russia" in result["fulfillmentMessages"][0]["text"]["text"][0]
            )
    
    def test_concerns_about_kremlin(self):
        """Test that question about Kremlin has Kremlin in answer"""
        app = Flask(__name__)

        with app.app_context():
            kremlin_request = get_test_request("concerns_kremlin")

            response = cloud_function(kremlin_request)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "Kremlin" in result["fulfillmentMessages"][0]["text"]["text"][0]
            )

if __name__ == "__main__":
    unittest.main()