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
        """Test that question about dogecoin has dogecoin in answer"""
        app = Flask(__name__)

        with app.app_context():
            test_2021 = get_test_request("How_much_tax_are_you_paying_after_selling_your_Tesla_stock")
            response = cloud_function(test_2021)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "2021" in result["fulfillmentMessages"][0]["text"]["text"][0]
            )

    def test_tax2018(self):
        """Test that question about portfolio has portfolio in answer"""
        app = Flask(__name__)

        with app.app_context():
            test_2018 = get_test_request("Is_it_true_that_you_paid_nothing_for_the_federal_income_tax_in_2018")
            response = cloud_function(test_2018)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "2018" in result["fulfillmentMessages"][0]["text"]["text"][0]
            )


if __name__ == "__main__":
    unittest.main()