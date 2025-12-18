from intents import intents
import datetime

def log_conversation(user, bot):
    with open("conversation_log.txt", "a", encoding="utf-8") as file:
        time = datetime.datetime.now()
        file.write(f"{time} - User: {user}\n")
        file.write(f"{time} - Bot: {bot}\n")

def get_response(user_input):
    user_input = user_input.lower()
    for intent in intents.values():
        for pattern in intent["patterns"]:
            if pattern in user_input:
                return intent["responses"][0]
    return "Sorry, I didn't understand that."

print("Chatbot started! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("Bot:", response)
    log_conversation(user_input, response)

    if "bye" in user_input:
        break
