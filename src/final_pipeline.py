from src.azure_demo import predict_live
from src.rasamodel import RasaChatbot
from utils.azure_models.azure_text_to_speech import AzureTextToSpeech
import time

# What is the closure reason for the alert with id [alertId]?


def come_on():
    # speech to text
    question = predict_live()
    # time.sleep(3)
    print(f"User: {question}")

    # bot from text
    ans = RasaChatbot().get_text(question)
    print(f"Bot: {ans}")

    # Speak Answer
    AzureTextToSpeech().synthesize_speech(ans)
    return ans


if __name__ == "__main__":
    main()
