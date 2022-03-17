import unittest
import sys
import os
import json
from flask import Flask
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "elonmusk"))

from tests.mock_dialogflow_utils import *

from elonmusk.main import cloud_function

class TestNeuralinkApp(unittest.TestCase):

    def test_nod(self):
        """Test that question about Nostalgia On Demand has 'Nostalgia On Demand' in answer"""
        app = Flask(__name__)

        with app.app_context():
            nod_request = get_test_request("neura_nostalgia")
            response = cloud_function(nod_request)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "Nostalgia On Demand" in result["fulfillmentMessages"][0]["text"]["text"][0]
            )

    def test_pain(self):
        """Test that question about pain elimination has 'pain elimination' in answer"""
        app = Flask(__name__)

        with app.app_context():
            pain_request = get_test_request("neura_pain")
            response = cloud_function(pain_request)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "pain elimination" in result["fulfillmentMessages"][0]["text"]["text"][0]
            )
    
    def test_AI(self):
        """Test that question about AI symbiosis has 'AI symbiosis' in answer"""
        app = Flask(__name__)

        with app.app_context():
            ai_request = get_test_request("neura_AI")
            response = cloud_function(ai_request)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "AI symbiosis" in result["fulfillmentMessages"][0]["text"]["text"][0]
            )
    
    def test_telepathy(self):
        """Test that question about telepathy has 'telepathy' in answer"""
        app = Flask(__name__)

        with app.app_context():
            tele_request = get_test_request("neura_tele")
            response = cloud_function(tele_request)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "telepathy" in result["fulfillmentMessages"][0]["text"]["text"][0]
            )
    
if __name__ == "__main__":
    unittest.main()