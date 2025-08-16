import random
import datetime

# Predefined responses (intent-based chatbot)
responses = {
    "greeting": [
        "Hello! How can I help you today?",
        "Hi there! 😊 What can I do for you?",
        "Hey! How's it going?"
    ],
    "name": [
        "I am PyBot, your personal assistant 🤖.",
        "You can call me PyBot!",
        "My name is PyBot, nice to meet you!"
    ],
    "age": [
        "I am timeless! But I was created in 2025 😉.",
        "I don’t age like humans, I just keep learning!",
    ],
    "time": [
        f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}",
        f"It’s {datetime.datetime.now().strftime('%I:%M %p')} right now."
    ],
    "weather": [
        "I can't fetch live weather yet, but I hope it's sunny ☀",
        "Weather is just perfect here in PyBot land!"
    ],
    "bye": [
        "Goodbye! Have a great day 👋",
        "Bye! See you soon 😃",
        "Take care, see you again!"
    ],
    "unknown": [
        "Hmm... I didn’t quite get that. Can you rephrase?",
        "Sorry, I don’t understand. Try asking differently.",
        "I’m still learning! Can you ask another way?"
    ]
}

# Intent keywords
intents = {
    "greeting": ["hi", "hello", "hey"],
    "name": ["your name", "who are you"],
    "age": ["your age", "how old"],
    "time": ["time", "clock"],
    "weather": ["weather", "temperature"],
    "bye": ["bye", "exit", "quit", "goodbye"]
}


def get_intent(user_input):
    """Match user input with intent keywords"""
    for intent, keywords in intents.items():
        for word in keywords:
            if word in user_input.lower():
                return intent
    return "unknown"


def chatbot():
    print("🤖 PyBot: Hello! I am your AI ChatBot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        intent = get_intent(user_input)

        # Random response from matched intent
        response = random.choice(responses[intent])
        print("🤖 PyBot:", response)

        if intent == "bye":
            break


if __name__ == "__main__":
    chatbot()