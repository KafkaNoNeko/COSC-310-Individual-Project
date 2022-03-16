import unittest
import sys
import os
import json
from flask import Flask
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "elonmusk"))

from tests.mock_dialogflow_utils import *

from elonmusk.main import cloud_function

class TestHasFullfilment(unittest.TestCase):

    def test_tesla(self):
        """Test that question about Tesla has Tesla in answer"""
        app = Flask(__name__)

        with app.app_context():
            tesla_request = get_test_request("what_tesla_does")
            response = cloud_function(tesla_request)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "Tesla" in result["fulfillmentMessages"][0]["text"]["text"][0]
            )
        
    
    def test_spacex(self):
        """Test that question about SpaceX has SpaceX in answer"""
        app = Flask(__name__)
        with app.app_context():
            spacex_request = get_test_request("tell_me_more_spacex")
            response = cloud_function(spacex_request)
            result = json.loads(response.get_data(as_text=True))
            
            self.assertTrue(
                "SpaceX" in result["fulfillmentMessages"][0]["text"]["text"][0]
            )

if __name__ == "__main__":
    unittest.main()