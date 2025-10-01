user_input = ["hello","how are you?","bye"]
predefined_replies = ["hi","I'm fine","Goodbye"]
def chat(user_input):
    if user_input == "hello":
        return predefined_replies[0]
    elif user_input == "how are you?":
        return predefined_replies[1]
    elif user_input == "bye":
        return predefined_replies[2]
    else:
        return "I don't understand"
print("Chatbot is running! (type 'bye' to exit)\n")
while True:
    user_text = input("You: ")
    reply = chat(user_text)
    print("Bot:", reply)
    if user_text == "bye":
        break