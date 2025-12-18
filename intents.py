intents = {
    "greeting": {
        "patterns": ["hi", "hello", "hey", "good morning", "good evening"],
        "responses": ["Hello! How can I help you?", "Hi there!", "Hey!"]
    },

    "small_talk": {
        "patterns": [
            "how are you",
            "how r u",
            "what's up",
            "how is life"
        ],
        "responses": [
            "I'm doing great! Thanks for asking 😊",
            "All good! How about you?"
        ]
    },

    "food": {
        "patterns": [
            "have you eaten",
            "did you eat",
            "had food",
            "had your lunch",
            "had dinner"
        ],
        "responses": [
            "I'm a bot 😄 I don't eat food, but I hope you did!",
            "I don't eat, but tell me what you had!"
        ]
    },

    "help": {
        "patterns": ["help", "assist", "support"],
        "responses": ["I can answer basic questions. Try asking about AI or food."]
    },

    "ai": {
        "patterns": [
            "what is ai",
            "define ai",
            "ai meaning"
        ],
        "responses": [
            "AI stands for Artificial Intelligence. It enables machines to mimic human intelligence."
        ]
    },

    "exit": {
        "patterns": ["bye", "exit", "quit"],
        "responses": ["Goodbye! Have a nice day 👋"]
    }
}

