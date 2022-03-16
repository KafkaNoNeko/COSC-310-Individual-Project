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