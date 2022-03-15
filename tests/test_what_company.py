import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from tests.mock_dialogflow_utils import *

from elonmusk.main import cloud_function

class TestHasFullfilment(unittest.TestCase):

    def test_tesla():
        """Test that response has the correct format for Dialogflow"""
        pass

        
    
    def test_spacex():
        """Test that response has the correct format for Dialogflow"""
        pass