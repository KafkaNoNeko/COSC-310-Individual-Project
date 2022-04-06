import urllib.parse

def map_search(text):
    """Extracts query from user-entered text and returns the associated Google maps link"""
    try: 
        # remove the word "map" and keep other keywords
        # this step is not really needed
        #query = text.lower().replace(" map", "")

        # encode to url
        query_url = urllib.parse.quote(query)

        link = "https://www.google.com/maps/search/?api=1&query=" + query_url

        result = "Here you go! \n" + link
    except:
        result = "I can't find it right now, but why not take a look at my new tweets first?"
    return result