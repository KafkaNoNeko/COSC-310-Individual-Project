import unittest
import sys
import os
import json
from flask import Flask
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "elonmusk"))

from tests.mock_dialogflow_utils import *

from elonmusk.main import cloud_function

class TestWhatIsCrypto(unittest.TestCase):

    def test_dogecoin(self):
        """Test that question about dogecoin has dogecoin in answer"""
        app = Flask(__name__)

        with app.app_context():
            test_dogecoin = get_test_request("What_is_special_about_doge")
            response = cloud_function(test_dogecoin)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "dogecoin" in result["fulfillmentMessages"][0]["text"]["text"][0]
            )

    def test_portfolio(self):
        """Test that question about portfolio has portfolio in answer"""
        app = Flask(__name__)

        with app.app_context():
            test_portfolio = get_test_request("What_does_portfolio_do")
            response = cloud_function(test_portfolio)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "portfolio" in result["fulfillmentMessages"][0]["text"]["text"][0]
            )

    def test_NTF(self):
        """Test that question about portfolio has portfolio in answer"""
        app = Flask(__name__)

        with app.app_context():
            test_NTF = get_test_request("What_is_NTF")
            response = cloud_function(test_NTF)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "test_NTF" in result["fulfillmentMessages"][0]["text"]["text"][0]
            )

if __name__ == "__main__":
    unittest.main()