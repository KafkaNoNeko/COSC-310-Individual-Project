import random


def handle_what_company_intent(query_result):
    """Returns list of text messages for the What Company Intent"""
    print(f"DEBUG: What Company Intent")

    try:
        company = query_result["parameters"]["Companies"]

        if company == "Tesla":
            return [
                """Tesla is accelerating the world's transition to sustainable 
                energy with electric cars - maybe you should buy one!"""
            ]
        elif company == "SpaceX":
            return [
                """SpaceX designs, manufactures and launches advanced rockets and spacecraft.
                Like NASA but much, much cooler.
                """
            ]
        elif company == "Paypal":
            return [
                """I did not found Paypal, but they bought my online bank and 
                made a popular payment system"""
            ]
        elif company == "The Boring Company":
            return [
                """The Boring Company creates safe, fast-to-dig, and low-cost
                transportation, utility, and freight tunnels"""
            ]
        elif company == "OpenAI":
            return ["OpenAI’s mission is to ensure that artificial general intelligence benefits all of humanity."]
        elif company == "Hyperloop":
            return [
                """Hyperloop is an ultra-high-speed public transportation system 
                in which passengers travel in autonomous electric pods at 600+ miles per hour"""
            ]
        elif company == "SolarCity":
            return [
                """SolarCity was the first solar company to let you purchase 
                solar power without having to pay for the panels. Nice."""
            ]
        elif company == "Neuralink":
            return [
                """We're developing high bandwidth brain-machine interfaces 
                to connect humans and machines at Neuralink"""
            ]
        else:
            return ["Sorry, I forgot I own that company!"]
    except:
        return ["My engineers are working on this right now - thanks for talking to Elon Musk Bot"]


def handle_WorkatSpaceXIntent_followup(query_result):
    """Returns list of text messages for the Work at SpaceX follow-up Intent"""
    print(f"DEBUG: Work at SpaceX follow-up Intent")

    try:
        position = query_result["parameters"]["position"]

        if position == "Software Engineer":
            return [
                """As a Software Engineer, you will be developing software solutions for complex engineering problems 
                across our SpaceX programs!"""
            ]
        elif position == "Web Developer":
            return [
                """As a Web Developer, you will shape user-centric products that are critical to our core messaging at SpaceX, 
                as well as the development and execution of our broadband satellite network Starlink."""
            ]
        elif position == "Electrical Engineer":
            return [
                """We have Hardware Development Electrical Engineer positions focusing on Failure Analysis, Payload, 
                and Satellite Bus Engineering. Regardless of the position you choose, you will contribute to our groudbreaking
                endeavours."""
            ]
        elif position == "Mechanical Engineer":
            return [
                """Mechanical Engineers are responsible for the continued development of critical components and 
                the overall structural design of SpaceX's spacecraft and satellites. You might not want to miss this 
                opportunity to contribute to humanity's space adventure!"""
            ]
        elif position == "Structural Analyst":
            return [
                """Structural Analysts test and maintain our technologies.  They play a critical role and should be able to think 
                on their feet."""
            ]
        else:
            return ["Sorry, I don't remember what the detailed job description is! Check it out here: www.spacex.com/careers/"]
    except:
        return ["My engineers are working on this right now - thanks for talking to Elon Musk Bot"]


def handle_daily_routine_intent(query_result):
    print(f"DEBUG: Daily Routine Intent")
    # Souce: https://finty.com/us/daily-routines/elon-musk/

    try:
        routine = query_result["parameters"]["routine"]

        if routine == 'Morning':
            return [random.choice([
                """I usually wake up at about 7am. I then take a shower and have a nice cup of coffee. I don't usually have breakfast because of my work. """,
                """I hate sleeping but I have to sleep for about 6 hours to be at my best performance. I usually start my morning with shower and coffee""",
                """I don't usually have breakfast since after waking up (usually at 7am) and coffee, I have to run to work."""
            ])]
        elif routine == 'Afternoon':
            return [random.choice([
                """Mostly work, I'll storm out if they BS-ing""",
                """Work, work, and work""",
                """I usually be at a state where I work without noticing the clock"""
            ])]
        elif routine == "Evening":
            return [random.choice([
                """Since I don't eat during the day, this is the time I consume my food and be with my child. Then work again. And finally Anime!""",
                """I will have some diet coke, play with my child, and jump into work at about 10pm and reward myself with Anime""",
                """I will sleep at 1am, before that, I eat, play with my kid, work, and watch Anime. Busy night, right?"""
            ])]
        elif routine == "freetime":
            return [random.choice([
                """Freetime? Never heard of that.""",
                """I work 80 to 100 hours a week, and family, what do you think?""",
                """Anime!"""
            ])]
        else:
            return [random.choice([
                """Don't be a paparazzi""",
                """Which news channel do you come from?""",
                """Book the real Elon Musk for question like this!"""
            ])]
    except:
        return ["My engineers are working on this right now - thanks for talking to Elon Musk Bot"]


def handle_NeuralinkAppIntent_followup(query_result):
    """Returns list of text messages for the Neuralink Applications follow-up Intent"""
    print(f"DEBUG: Neuralink Applications follow-up Intent")
    
    try:
        app = query_result["parameters"]["NeuralinkApp"]

        if app == "nostalgia on demand":
            return [
                """Ever had blurry memories of important moments of your life? The Link will eliminate these and 
                enable you to exactly relive memories as if you travelled back to in time. This is what I call 
                Nostalgia On Demand."""
            ]
        elif app == "pain elimination":
            return [
                """Oh, pain elimination! A world without pain, the source of all human suffering, who would reject it? The Link will enable its 
                user to kill any pain they feel."""
            ]
        elif app == "AI symbiosis":
            return [
                """Achieving an AI symbiosis is vital to humanity from an existential threat perspective. We need to be prepared."""
            ]
        elif app == "telepathy":
            return [
                """This would be what I call 'non-linguistic consent consensual conceptual telepathy'. Putting our thoughts
                into words not only requires a tremendous amount of effort, but also does not accurately describe what we are
                really thinking. Telepathy can be the game changer!"""
            ]
        else:
            return ["Sorry, this might not be currently on our list, but it is worth considering. Stay tuned for more exciting news!"]
    except:
        return ["My engineers are working on this right now - thanks for talking to Elon Musk Bot"]
