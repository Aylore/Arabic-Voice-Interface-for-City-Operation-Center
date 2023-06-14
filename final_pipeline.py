from src.speechtotext.google_speech_to_text import GoogleSpeechToText
from src.speechtotext.azure_speech_to_text import AzureSpeechToText

from src.texttospeech.google_text_to_speech import GoogleTextToSpeech
from src.texttospeech.azure_text_to_speech import AzureTextToSpeech

from src.rasa.rasamodel import RasaChatbot
from utils.main_helper import assert_english, assert_user_language


def main(path=None):
    # 1- Speech to Text (getting the client question)
    question = AzureSpeechToText(path).transcribe()
    print(f"User: {question}")

    # 1.1 - Assert the question in English For the chatbot
    user_language, english_question = assert_english(question)
    print(f"User Language: {user_language}\nEnglishQuestion: {english_question}")

    # 2- Bot Answer
    answer = RasaChatbot().response(english_question)

    # 2.2- Assert the Answer in User Language
    answer_user_language = assert_user_language(user_language, answer)
    print(f"Bot: {answer_user_language}")

    # 3- Text To Speech Answer
    result = AzureTextToSpeech(answer_user_language).read_aloud()

    response = f"Your Question: {question}\nAnswer: {answer_user_language}"
    return response


if __name__ == "__main__":
    live = True

    if live:
        print(main())
    else:
        path = "utils/audio_samples/audio1.wav"
        main(path)
