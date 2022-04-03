# import secret credentials
from credentials import *
import tweepy as tw
import re
import spacy
import random as rd

def find_hyperlink(text):
    """ Returns hyperlink if any
        Adapted from: https://stackoverflow.com/questions/839994/extracting-a-url-in-python
    """
    try: 
        link = re.search("(?P<url>https?://[^\s]+)", text).group("url")
        link = link[:-1]    #remove the '
    except:
        link = ""
    return link

def extract_topic(text):
    """ Returns the topic of the tweet using NLP
        Analysis using POS Tagging (entity recognition does not seem to work too well)
    """

    try:
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)

        topic = ""
        for np in doc.noun_chunks:
            if (find_hyperlink(str(np)) != ""):         # ignore hyperlinks
                continue 

            if len(np) > len(topic):                    # keep longest chunk
                topic = np
    
    except: 
        topic = "things I find interesting or relevant"   
    return topic

def choose_topic(topics):
    """Randomly choose a topic from the list
    """
    return rd.choice(topics)

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
                                count=20,
                                include_rts = False,     # no retweets
                                exclude_replies=True,
                                tweet_mode = 'extended'  # keep full text
                                )

       
        # analyse tweets 
        topics = []                                             # for choosing best topic
        topic_link = {}                                         # store topics and associated links if any
        for tweet in tweets[:20]:
            tweet = tweet._json['full_text'].encode('utf-8')    # need to encode to UTF-8 
            tweet = str(tweet)[2:]                              # convert b'' to string
            
            tw_topic = extract_topic(tweet)
            topics.append(tw_topic)
            topic_link[tw_topic] = find_hyperlink(tweet)

        # choose topic 
        topic = choose_topic(topics)

        # generate response
        result = "I love Twitter. Recently, I've been tweeting about "
        result = result + str(topic)
        
        # add link if any
        link = topic_link[topic]
        if (link != ""):
            result = result + ". You can check out this link: " + link

        return result

    except:
            return "My engineers are working on this right now - thanks for talking to Elon Musk Bot"
            



