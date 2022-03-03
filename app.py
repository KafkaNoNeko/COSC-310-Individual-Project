from flask import Flask, request, render_template, jsonify
import json
import os

app = Flask(__name__, template_folder='template')

# Start a  web server
@app.route("/")
def index():
    return render_template('index.html')

# When the user presses enter, the message in the chatbox will be sent to the server through a POST request to /api/chat
@app.route("/api/chat", methods=["POST"])
def chat():
    user_input = request.form["user_input"]
    chatbot_response = chat_bot_response(user_input)
    return jsonify({"chatbot_response": chatbot_response})

# This function is used to handle the chatbot response
def chat_bot_response(user_input: str) -> str:
    # load the keywords and answers from the json file
    with open(os.path.join(os.path.dirname(__file__), "data.json"), "r") as f:
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

if __name__ == "__main__":
    app.run(debug=True)
