# Simple Rule-Based Chatbot

def chatbot():
    print("Chatbot: Hello! I’m your friendly chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()   # take user input and convert to lowercase

        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hi there!")
        elif user_input in ["how are you", "how are you doing"]:
            print("Chatbot: I’m fine, thanks for asking! How about you?")
        elif user_input in ["i am fine", "i'm good", "fine"]:
            print("Chatbot: That’s great to hear!")
        elif user_input in ["what is your name", "who are you"]:
            print("Chatbot: I’m a simple rule-based chatbot made using Python.")
        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a nice day 😊")
            break
        else:
            print("Chatbot: Sorry, I didn’t understand that.")

# Run the chatbot
chatbot()
