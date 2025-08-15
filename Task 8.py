# Simple Rule-Based Chatbot using if-else

print("Welcome to ChatBot 1.0! (type 'bye' to exit)")
print("------------------------------------------------")

while True:
    user_input = input("You: ").lower().strip()  # Take user input and normalize
    
    # Exit condition
    if user_input == "bye":
        print("ChatBot: Goodbye! Have a great day!")
        break

    # Responses based on keywords
    if "hello" in user_input or "hi" in user_input:
        print("ChatBot: Hello there! How can I help you today?")
    
    elif "how are you" in user_input:
        print("ChatBot: I'm doing great, thanks for asking! How about you?")
    
    elif "your name" in user_input:
        print("ChatBot: I’m ChatBot 1.0, your friendly virtual assistant.")
    
    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"ChatBot: The current time is {current_time}.")
    
    elif "weather" in user_input:
        print("ChatBot: I can't check live weather yet, but I hope it's sunny where you are!")
    
    elif "joke" in user_input:
        print("ChatBot: Why don’t skeletons fight each other? They don’t have the guts! 😂")
    
    else:
        print("ChatBot: Sorry, I didn’t understand that. Can you rephrase?")
