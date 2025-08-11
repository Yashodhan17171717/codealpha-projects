def chatbot():
    print("Chatbot: Hello! I'm your chatbot. Type 'bye' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hey there! How can I help you?")
        elif user_input in ["how are you", "how are you doing"]:
            print("Chatbot: I'm doing well, thanks! And you?")
        elif user_input in ["what's your name", "who are you"]:
            print("Chatbot: I'm a simple chatbot here to chat with you.")
        elif user_input in ["what can you do", "what do you do"]:
            print("Chatbot: I can respond to some basic questions. Feel free to ask!")
        elif user_input in ["thank you", "thanks"]:
            print("Chatbot: You're welcome!")
        elif user_input in ["can you help me", "i need help"]:
            print("Chatbot: Sure! What do you need help with?")
        elif user_input in ["bye", "goodbye", "exit"]:
            print("Chatbot: Goodbye! It was nice talking to you.")
            break
        else:
            print("Chatbot: Hmm... I don't know how to respond to that yet.")

chatbot()
