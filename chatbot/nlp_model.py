import random

def get_bot_response(message):
    message = message.lower()

    responses = {
        "hello": ["Hello! How can I help you?", "Hi there!"],
        "ai": ["AI stands for Artificial Intelligence."],
        "flower": ["A flower is the reproductive part of a plant."],
        "humanity": ["Humanity refers to human beings collectively."]
    }

    for key in responses:
        if key in message:
            return random.choice(responses[key])

    return "Sorry, I don't understand. Please ask something else."