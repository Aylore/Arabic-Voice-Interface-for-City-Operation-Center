import requests


class RasaChatbot:
    def __init__(self, endpoint="http://localhost:5005/webhooks/rest/webhook"):
        self.endpoint = endpoint

    def send_message(self, message):
        data = {
            "message": message,
        }
        response = requests.post(self.endpoint, json=data)
        return response.json()

    def chat(self):
        while True:
            user_input = input("User: ")
            response = self.send_message(user_input)

            # Extract the bot's response
            if response:
                bot_response = response[0]["text"]
                print("Bot:", bot_response)

                # Check if the bot has a follow-up action
                if "next_action" in response[0]:
                    # Wait for the bot to finish its action
                    while True:
                        response = self.send_message("")

                        if (
                            response
                            and "event" in response[0]
                            and response[0]["event"] == "action"
                        ):
                            # Action completed, get the bot's next response
                            bot_response = response[0]["text"]
                            print("Bot:", bot_response)
                            break

    def response(self, text):
        response = self.send_message(text)
        try:
            bot_response = response[0]["text"]
        except:
            bot_response = 'Sorry, Can you repeat the question?'
        return bot_response


if __name__ == "__main__":
    # Example usage
    endpoint = "http://localhost:5005/webhooks/rest/webhook"
    chatbot = RasaChatbot(endpoint)
    chatbot.chat()
