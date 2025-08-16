from textblob import TextBlob

def mood_checker():
    print("🤖 AI Mood Detector")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("🤖 Thanks for using Mood Detector. Take care! 👋")
            break

        # Sentiment Analysis using TextBlob
        analysis = TextBlob(user_input)
        polarity = analysis.sentiment.polarity  # -1 (negative) to +1 (positive)

        # Detect mood based on polarity
        if polarity > 0.5:
            mood = "😄 You seem very Happy / Excited!"
        elif polarity > 0:
            mood = "🙂 You are in a Positive mood!"
        elif polarity == 0:
            mood = "😐 Seems Neutral."
        elif polarity > -0.5:
            mood = "😟 You sound a bit Sad."
        else:
            mood = "😡 You seem Angry / Upset!"

        print("🤖 AI Mood Detector:", mood)

# Run program
if __name__ == "__main__":
    mood_checker()