import unittest
import sys
import os
import json
from flask import Flask
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "elonmusk"))

from tests.mock_dialogflow_utils import *

from elonmusk.main import cloud_function

class TestWorkAtSpaceX(unittest.TestCase):

    def test_swe(self):
        """Test that question about Software Engineer has Software Engineer in answer"""
        app = Flask(__name__)

        with app.app_context():
            swe_request = get_test_request("spacex_swe")
            response = cloud_function(swe_request)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "Software Engineer" in result["fulfillmentMessages"][0]["text"]["text"][0]
            )

    def test_webdev(self):
        """Test that question about Web Developer has Web Developer in answer"""
        app = Flask(__name__)

        with app.app_context():
            webdev_request = get_test_request("spacex_webdev")
            response = cloud_function(webdev_request)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "Web Developer" in result["fulfillmentMessages"][0]["text"]["text"][0]
            )    
            
            
    def test_eeng(self):
        """Test that question about Electrical Engineer has Electrical Engineer in answer"""
        app = Flask(__name__)

        with app.app_context():
            eeng_request = get_test_request("spacex_eeng")
            response = cloud_function(eeng_request)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "Electrical Engineer" in result["fulfillmentMessages"][0]["text"]["text"][0]
            )    

    def test_meng(self):
        """Test that question about Mechanical Engineer has Mechanical Engineer in answer"""
        app = Flask(__name__)

        with app.app_context():
            meng_request = get_test_request("spacex_meng")
            response = cloud_function(meng_request)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "Mechanical Engineer" in result["fulfillmentMessages"][0]["text"]["text"][0]
            )    
    
    def test_sa(self):
        """Test that question about Structural Analyst has Structural Analyst in answer"""
        app = Flask(__name__)

        with app.app_context():
            sa_request = get_test_request("spacex_sa")
            response = cloud_function(sa_request)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "Structural Analyst" in result["fulfillmentMessages"][0]["text"]["text"][0]
            )    

if __name__ == "__main__":
    unittest.main()