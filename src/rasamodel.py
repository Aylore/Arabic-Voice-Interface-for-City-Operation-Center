import requests

class RasaChatbot:
    def __init__(self, endpoint):
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
                bot_response = response[0]['text']
                print("Bot:", bot_response)

# Example usage
endpoint = "http://localhost:5005/webhooks/rest/webhook" 
chatbot = RasaChatbot(endpoint)
chatbot.chat()