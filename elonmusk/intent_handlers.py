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


def handle_crypto_advice_intent(query_result):
    """Returns list of text messages for the Crypto Advice Intent"""
    print(f"DEBUG: Crypto Advice Intent")

    try:
        crypto = query_result["parameters"]["crypto"]

        if crypto == "dogecoin":
            return [
                """I don’t particularly support any crypto except dogecoin for a reason. 
                Lots of people I talked to on the production lines at Tesla or building rockets at SpaceX own Doge. 
                They aren’t financial experts or Silicon Valley technologists. 
                That’s why I decided to support Doge — it felt like the people’s crypto."""
            ]
        elif crypto == "crypto":
            return [
                """Don’t bet the farm on crypto! 
                True value is building products & providing services to your fellow human beings, not money in any form.
                """
            ]
        elif crypto == "portfolio":
            return [
                """That will reduce the risk if one or more  perform poorly, but cryptos are high in risk itself. 
                The cryptos I am holding are limited to Bitcoin, Ethereum and Dogecoin."""
            ]
        else:
            return [ f'Check my tweets about {crypto}, you\'ll find the answer !']
    except:
        return ["My engineers are working on this right now - thanks for talking to Elon Musk Bot"]

def handle_what_is_crypto_intent(query_result):
    """Returns list of text messages for the What is Crypto Intent"""
    print(f"DEBUG: What is Crypto Intent")

    try:
        crypto = query_result["parameters"]["crypto"]

        if crypto == "dogecoin":
            return [
                """The point is that dogecoin was invented as a joke, essentially to make fun of cryptocurrency. 
                Fate loves irony. The currency that started as a joke in fact becomes the real currency. To the moon!"""
            ]
        elif crypto == "portfolio":
            return [
                """A cryptocurrency portfolio is a means to manage your inventory of online currency investments. 
                It can be hosted on a cryptocurrency management software that helps you track each coin's performance 
                and provides you with analytical tools.
                """
            ]
        elif crypto == "NFT":
            return [
                """NFTs are unique cryptographic tokens that exist on a blockchain and cannot be replicated."""
            ]
        else:
            return ["""It is any form of currency that exists virtually and uses cryptography to secure transactions. 
                    Cryptocurrencies don't have a central issuing or regulating authority. 
                    Instead, they use a decentralized system to record transactions and issue new units."""]
    except:
        return ["My engineers are working on this right now - thanks for talking to Elon Musk Bot"]

def handle_billionaire_tax_intent(query_result):
    """Returns list of text messages for the Billionaire Tax Intent"""
    print(f"DEBUG: Billionaire Tax Intent")

    try:
        crypto = query_result["parameters"]["Tax"]

        if crypto == "2021":
            return [
                """I will pay more taxes than any American in history in 2021."""
            ]
        elif crypto == "2018":
            return [
                """That’s a funny joke."""
            ]
        else:
            return ["""My wealth ‘isn’t some deep mystery. My taxes are super simple, and I pay them."""]
    except:
        return ["My engineers are working on this right now - thanks for talking to Elon Musk Bot"]