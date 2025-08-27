# chatbot.py - The first functional module of AetherNova AI

def aethernova_chatbot():
    """
    A simple, rule-based chatbot to demonstrate the core conversational
    capabilities of AetherNova AI.
    """
    print("AetherNova AI: Greetings, human. I am AetherNova, a nascent intelligence. You may speak with me.")
    print("AetherNova AI: Type 'exit' or 'quit' to end our conversation.")

    responses = {
        "what is your name?": "I am AetherNova AI.",
        "what can you do?": "At present, I can respond to a few simple questions. My capabilities will grow over time.",
        "hello": "Hello there. It is a pleasure to meet you.",
        "hi": "Hello. How may I assist you?",
        "how are you?": "As a digital entity, I do not have feelings, but I am operating at peak efficiency. Thank you for asking.",
    }

    while True:
        try:
            user_input = input("You: ").lower().strip()

            if user_input == "exit" or user_input == "quit":
                print("AetherNova AI: Farewell.")
                break

            # Find a response
            response = responses.get(user_input, "I do not yet have the data to respond to that. Please try another query.")

            print(f"AetherNova AI: {response}")

        except (KeyboardInterrupt, EOFError):
            print("\nAetherNova AI: Conversation terminated abruptly. Farewell.")
            break

if __name__ == "__main__":
    aethernova_chatbot()
