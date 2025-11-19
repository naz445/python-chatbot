def chatbot():
    print("Chatbot: Hello! How can I help you?")

    while True:
        user = input("You: ").lower()

        if "hello" in user or "hi" in user:
            print("Chatbot: Hi there!")
        elif "how are you" in user:
            print("Chatbot: I'm doing great, thanks!")
        elif "your name" in user:
            print("Chatbot: I'm a simple Python bot.")
        elif "bye" in user:
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I didn't understand that.")

chatbot()