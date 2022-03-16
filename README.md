# Elon Musk Bot ![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54) ![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=logo=telegram&logoColor=white) ![Flask](https://img.shields.io/badge/flask-%23000.svg?logo=flask&logoColor=white)

<p align="center"> 
<img width="620" height="414" src="static/img/ElonMusk.png">
</p>

Elon Musk Bot is a chatbot inspired by the entrepreneur and billionaire Elon Musk. It can answer questions about Tesla, SpaceX, cryptocurrencies - give it a try!

## Setting Up

To launch the Elon Musk bot, first [install Python](https://realpython.com/installing-python/) on your machine. Once Python is installed, launch your terminal on the folder containing the repository and run:

```
pip install -r requirements.txt
```

## Creating your own Telegram bot based on this code

To create your own Telegram bot, first go to https://t.me/botfather. Send the following message to Botfather:

```
/newbot
```

Botfather will ask you for the name and the username for your bot. After you pick the two, you will receive a message along this lines:

```
Done! Congratulations on your new bot. You will find it at t.me/LINK_TO_YOUR_BOT. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
HERE_IS_YOUR_LONG_SECRET_TOKEN
Keep your token secure and store it safely, it can be used by anyone to control your bot.
```

Then, copy the secret token to a file named `env.yaml` at the root of this repository as follows:

```yaml
TOKEN: "HERE_IS_YOUR_LONG_SECRET_TOKEN"
```

Obviously, replace "HERE_IS_YOUR_LONG_SECRET_TOKEN" with the real token you got from Botfather. Once that is done and you saved `env.yaml`, make sure you have installed Python and the requirements:

```
pip install -r requirements.txt
```

Then, run the Telegram bot:

```
python src/app.py
```

Lastly, go to t.me/LINK_TO_YOUR_BOT (the link you obtained from Botfather) and chat with the bot! 

## Code Structure

```
    .
    ├── app.py                    # Code for the Python back-end - it handles requests to the bot
    ├── elon_musk_bot.py          # Code for the Telegram bot - it handles Telegram requests
    ├── data.json                 # Answers to the predefined topics Elon Musk bot can answer
    ├── template                  # Contains the front-end logic for the user interace
    └── README.md                 # This file!
```

## Features added in Assignment 3

### GUI Improvements

We used the platform of telegram as a way of giving a face to our bot, byincorporating the already popular and polished platform were able to vastly improve on the GUI of the systrm and user experience as well as a platform for the user to reference ast interactions.

### Improvements using language toolkits

* **Synonym Recognition**: By being able to recognize common synonyms used by the user, the bot is a able to respond to a wider amount of inpputs and the user experiecne is enriched as they get a greater freedom when it comes to choosing how they phrase their question. This allows them to have a more natural conversation with the bot. as seen below, we are able to use red in place of crimson and the bot can still provide an accurate answer
    <p align="center"> 
    <img width="1252" height="214" src="static/img/synonym.png">
    </p>
* **Entity analysis**: By enabling the bot to pick out proper nouns used in the conversation we are abke to improve the accuracy of the bot's responses by guaging the topic of conversation quicker than earlier. Thereby we save the user fom having to repeat themselves and improve their overall experience. as seen below, the bot is able to understand Tesla and Model S as entities.
    <p align="center"> 
    <img width="1252" height="213" src="static/img/entity.png">
    </p>
* **Sentiment analysis**: With the help of dialogflow's sentimental analysis capabilities we are able to look beyond what the user is saying and try and respond closer to what they mean. Ideally, this gives our bot a more human touch and as a result improves user interation and experience.
  **add snippet**

### Github Repo with commit history

Link to repo: https://github.com/cosc-310-group32/Assignment3/tree/main .
The branch structure **as of 2022-03-15** can be found below.
<p align="center"> 
<img width="1223" height="448" src="static/img/branch.png">
</p>

### Extra topics and out of scope responses

We have added support for other companies operated or started by elon music as opposed to our original set and thereby increased the useability of our bot. Secondly we have also accounted for the fact that the bot does not have allencompasing knowledge and as a result we have included responses that can be used when the bot encounters unknown querys to help keep the flow of the conversation and provide useful feedback to the user.  

### Level 0 data flow diagram

The Level 0 diagram can be found below:
<p align="center"> 
<img width="1480" height="421" src="static/img/lvl0DFD.png">
</p>

Explaination: When the user first connects to the bot they send a message to dialogflow which passes it on to the bot to start the session. Every question asked by the user is analysed by dialogflow and then parsed to the bot once it has been converted to it's closest match on the database. The bot then returns the result based on the closest match and that result is sent over to the user through dialogflow.  

### Level 1 data flow diagram

The level 1 dataflow diagram can be found below:
<p align="center"> 
<img width="1635" height="960" src="static/img/lvl1DFD.png">
</p>

Explaination: When the user connects to dialogflow using telegram, they send a start bot message that is passed on to the bot to start the session as a closest matched question. Every subsiquent query is analysed for synonyms, sentiment and entities while beong processed and dialogflow finds the closest match to the processed query from the database of information that is available to the bot. This question is then sent to the bot which then looks up the answer and responds with the answer to the question. This answer is, in turn, displayed to the user on the telegram GUI.

### Sample output and Limitations

**todo**

### Possible API Branches

* Synonym recognition process
* Entity recognition process
* closest match to queston using processed query can be applied to any database.
* Sentiment analysis.
* Our dialogflow impelemtation can be plugged into most telegram bots with relative ease and can act as the backbone for other bots.

## Built With

* [Python](https://www.python.org/) - Back End

## Authors

- [Kiet Phan](https://github.com/ketphan02)
- [Ivan Carvalho](https://github.com/IvanIsCoding)
- [Lydia Lin](https://github.com/yuqi88)
- [Akshat Singal](https://github.com/aksingal-dev)
- [Paula Wong-Chung](https://github.com/KafkaNoNeko)

