import os
import json

# This function is used to handle the chatbot response
def chat_bot_response(user_input: str) -> str:
    with open(os.path.join(os.path.dirname(__file__), "..", "..", "static", "json", "data.json"), "r") as f:
        data = json.load(f)
    
    max_item = {
        "value": 0,
        "answer": None
    }

    # loop through all the set of keywords and answers
    for item in data["items"]:
        cnt = 0
        for keyword in item["keywords"]:
            # if the keyword matches with some word in the user input, increase the count
            if keyword in user_input.lower():
                cnt += 1
        # if the current set of keywords matches more than the previous one (more keywords match), then use the answer corresponding to this set of keywords
        if cnt > max_item["value"]:
            max_item = {
                "value": cnt,
                "answer": item["answer"]
            }

    # this is used to handle the case when no keywords match with the user input    
    if max_item["value"] == 0:
        return "Sorry, I don't understand what you mean. Can you ask another question?"
    
    # return the answer corresponding to the keywords (having the maximum count)
    return max_item["answer"]