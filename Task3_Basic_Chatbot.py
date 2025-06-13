# Basic Chatbot
def chatbot():
    print("Chatbot is ready! (Type 'bye' to exit)\n")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "hello":
            print("Chatbot: Hi there!")
        elif user_input == "hi":
            print("Chatbot: Hello!")
        elif user_input == "how are you":
            print("Chatbot: I'm doing well, thanks!")
        elif user_input == "what's your name":
            print("Chatbot: I'm a simple Python chatbot.")
        elif user_input == "thanks":
            print("Chatbot: You're welcome!")
        elif user_input == "thank you":
            print("Chatbot: Glad to help!")
        elif user_input == "help":
            print("Chatbot: Try saying hello, asking how I am, or saying bye.")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: Sorry, I didn't understand that.")

# Start the chatbot
chatbot()

