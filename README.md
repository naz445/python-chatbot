# Python Rule-Based Chatbot

A simple Python-based rule-driven chatbot designed to demonstrate fundamental concepts in natural language processing, pattern recognition, and command-based interaction.  
This project showcases beginner-to-intermediate level chatbot architecture using conditional logic, keyword matching, and clean CLI formatting.

---

## Features

- Rule-based conversational engine  
- Keyword detection for intelligent responses  
- Multiple built-in commands:
  - Greetings  
  - Weather-related questions  
  - Asking the chatbot's name  
  - Asking how the chatbot is feeling  
  - Help command  
  - Exit/Goodbye command  
- Default fallback response for unknown inputs  
- User-friendly terminal interface  

---

## Technologies Used

- Python 3  
- Conditional rule-based logic  
- CLI interaction  

---

## How It Works

The chatbot processes user input and checks for keywords using a structured rule-based engine:

1. User types a message in the terminal  
2. Input is converted to lowercase  
3. Chatbot scans for known keywords  
4. Matching rule triggers the appropriate response  
5. If no rule is matched, the default fallback message is returned  

### Core Function: `chatbot_response()`

Handles:
- Keyword matching  
- Rule selection  
- Response generation  

### Main Loop

The program runs in a loop until the user types `"bye"`.

---
Simple Python Chatbot
Type ‘bye’ to exit.

You: hello
Chatbot: Hello! How can I assist you today?

You: what’s the weather
Chatbot: I cannot check real-time weather, but it seems like a nice day to code!

You: your name?
Chatbot: I am a simple Python chatbot created for learning purposes.
You: bye
Chatbot: Goodbye!
---

## Future Improvements

- Sentiment analysis support  
- Regex-based intent detection  
- NLP integration using NLTK or spaCy  
- Live API-based weather responses  
- GUI version using Tkinter  

---

## License

This project is released under the MIT License.
## Sample Output
