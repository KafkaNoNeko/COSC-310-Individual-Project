from elonmusk.intent_handlers import *

def cloud_function(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    from flask import jsonify
    request_json = request.get_json()
    print(f"DEBUG: {request_json}")
    
    intent_dictionary = {
        "What Company Does Intent": handle_what_company_intent,
        "Work at SpaceX Intent - custom": handle_WorkatSpaceXIntent_followup,
        "Crypto Advice Intent": handle_crypto_advice_intent,
        "What is Crypto Intent": handle_what_is_crypto_intent,
        "Billionaire Tax Intent": handle_billionaire_tax_intent,
        "Daily Routine Intent": handle_daily_routine_intent,
        "Neuralink Applications Intent - custom": handle_NeuralinkAppIntent_followup,
        "Fight Putin Intent": handle_fight_putin_intent,
        "Stand With Ukraine Intent": handle_stand_with_ukraine_intent,
        "Tweet Intent": handle_tweet_intent
    }

    try:
        query_result = request_json["queryResult"]
        user_intent = query_result["intent"]["displayName"]

        if user_intent in intent_dictionary:
            answer_list = intent_dictionary[user_intent](query_result)
        else:
            answer_list = ["My engineers are working on this right now - thanks for talking to Elon Musk Bot"]
    except:
        answer_list = ["My engineers are working on this right now - thanks for talking to Elon Musk Bot"]

    answer = {
      "fulfillmentMessages": [
        {"text": {"text": answer_list}}
      ]
    }

    return jsonify(answer)
