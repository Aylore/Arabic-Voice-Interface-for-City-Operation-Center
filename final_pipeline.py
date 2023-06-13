from src.texttospeech.azure_text_to_speech import AzureTextToSpeech
from src.speechtotext.azure_speech_to_text import AzureSpeechToText

from src.texttospeech.google_text_to_speech import GoogleTextToSpeech
from src.texttospeech.azure_text_to_speech import AzureTextToSpeech

from src.rasa.rasamodel import RasaChatbot


def main(path=None):
    # 1- Speech to Text (getting the client question)
    question = AzureSpeechToText(path).transcribe()
    print(f"User: {question}")

    # 2- Bot Answer
    answer = RasaChatbot().response(question)
    print(f"Bot: {answer}")

    # 3- Text To Speech Answer
    result = AzureTextToSpeech(answer).read_aloud()

    response = f'Your Question: {question}\nAnswer: {answer}'
    return response


if __name__ == "__main__":
    live = True

    if live:
        main()
    else:
        path = "utils/audio_samples/audio1.wav"
        main(path)
