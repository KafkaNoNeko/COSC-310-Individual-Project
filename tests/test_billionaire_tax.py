import unittest
import sys
import os
import json
from flask import Flask
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "elonmusk"))

from tests.mock_dialogflow_utils import *

from elonmusk.main import cloud_function

class TestBillionaireTax(unittest.TestCase):

    def test_tax2021(self):
        """Test that question about 2021 tax has 2021 in answer"""
        app = Flask(__name__)

        with app.app_context():
            test_2021 = get_test_request("tax2021")
            response = cloud_function(test_2021)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "2021" in result["fulfillmentMessages"][0]["text"]["text"][0]
            )

    def test_tax2018(self):
        """Test that question about the 2018 tax yields a funny joke response"""
        app = Flask(__name__)

        with app.app_context():
            test_2018 = get_test_request("tax2018")
            response = cloud_function(test_2018)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "joke" in result["fulfillmentMessages"][0]["text"]["text"][0]
            )


if __name__ == "__main__":
    unittest.main()