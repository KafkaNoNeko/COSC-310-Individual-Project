import unittest
import sys
import os
import json
from flask import Flask
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "elonmusk"))

from elonmusk.main import cloud_function
from tests.mock_dialogflow_utils import *

class TestDailyRoutine(unittest.TestCase):

    def test_morning(self):
        """Test that question about Morning has coffee or work or shower of 7am in answer"""
        app = Flask(__name__)

        with app.app_context():
            morning_request = get_test_request("dailyroutine_moring")
            response = cloud_function(morning_request)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "coffee" or "work" or "shower" or "7am" in result["fulfillmentMessages"][0]["text"]["text"][0].lower(
                )
            )
            self.assertEqual(
                response.status_code,
                200
            )

    def test_evening(self):
        """Test that question about Evening has anime or children or work in answer"""
        app = Flask(__name__)

        with app.app_context():
            evening_request = get_test_request("dailyroutine_evening")
            response = cloud_function(evening_request)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "anime" or "child" or "work" in result["fulfillmentMessages"][0]["text"]["text"][0].lower(
                )
            )
            self.assertEqual(
                response.status_code,
                200
            )

    def test_afternoon(self):
        """Test that question about Noon has Afternoon in answer"""
        app = Flask(__name__)

        with app.app_context():
            afternoon_request = get_test_request("dailyroutine_afternoon")
            response = cloud_function(afternoon_request)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "work" in result["fulfillmentMessages"][0]["text"]["text"][0].lower()
            )
            self.assertEqual(
                response.status_code,
                200
            )


if __name__ == "__main__":
    unittest.main()
