import json
import os

class MockRequest:

    def __init__(self, data, name):
        self.data = data
        self.name = name
    
    def get_json(self):
        return self.data

def get_json_test_data(name):
    path_to_json = os.path.join(
        os.path.dirname(__file__), "..", "data", f"{name}.json"
    )
    json_file = open(path_to_json)

    return json.load(json_file)

def get_test_request(name):
    data = get_json_test_data(name)

    return MockRequest(data, name)
