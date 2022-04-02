# import secret credentials
from credentials import *
import tweepy as tw
import re

def find_hyperlink(text):
    """ Returns hyperlink if any
        Adapted from: https://stackoverflow.com/questions/839994/extracting-a-url-in-python
    """
    try: 
        link = re.search("(?P<url>https?://[^\s]+)", text).group("url")
    except:
        link = ""
    return link 

def extract_topic(text):
    """ Returns the topic of the tweet using NLP
        
    """

    try:
        topic = "aaa"    
    
    except: 
        topic = "aaa" 
    return topic

def twitter_parse():
    """
    This function pulls Elon's latest tweets (excluding retweets, replies) and parses them 
    to extract meaningful information to be included in the conversation.
    """
    try:
        userid = "elonmusk"

        #Twitter credentials authorisation
        auth = tw.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tw.API(auth)

        tweets = api.user_timeline(screen_name=userid, 
                                count=50,
                                include_rts = False,     # no retweets
                                exclude_replies=True,
                                tweet_mode = 'extended'  # keep full text
                                )

       
        result = ""
        for tweet in tweets[:50]:
            tweet = tweet._json['full_text'].encode('utf-8')    # need to encode to UTF-8 
            tweet  = str(tweet)                                 # convert b'' to string
            result = tweet              # for testing

        # change this later
        return result

    except:
            return "My engineers are working on this right now - thanks for talking to Elon Musk Bot"
            



