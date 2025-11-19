def chatbot_response(user_input):

    text = user_input.lower()

    # Greeting
    if "hello" in text or "hi" in text:
        return "Hello! How can I assist you today?"

    # Weather (generic answer since no API)
    elif "weather" in text:
        return "I cannot check real-time weather, but it seems like a nice day to code!"

    # Name
    elif "your name" in text:
        return "I am a simple Python chatbot created for learning purposes."

    # Feeling
    elif "how are you" in text:
        return "I am functioning well! Ready to assist."

    # Help command
    elif "help" in text:
        return "You can ask about weather, greetings, my name, or say goodbye."

    # Goodbye
    elif "bye" in text or "goodbye" in text:
        return "Goodbye! Have a great day."

    # Default response
    else:
        return "I'm not sure how to respond to that, but I am learning!"


def main():
    print("Simple Python Chatbot")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break

        print("Chatbot:", chatbot_response(user_input))


main()
