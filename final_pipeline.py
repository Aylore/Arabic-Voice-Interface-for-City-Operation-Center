from src.speechtotext.google_speech_to_text import GoogleSpeechToText
from src.speechtotext.azure_speech_to_text import AzureSpeechToText

from src.texttospeech.google_text_to_speech import GoogleTextToSpeech
from src.texttospeech.azure_text_to_speech import AzureTextToSpeech

from src.rasa.rasamodel import RasaChatbot
from utils.main_helper import assert_english, assert_user_language
from src.wav2lip.inference import main as Wav2LipDiscriminator


def main(path=None):
    # 1- Speech to Text (getting the client question)
    question = AzureSpeechToText(path).transcribe()
    print(f"User: {question}")

    # 1.1 - Assert the question in English For the chatbot
    user_language, english_question = assert_english(question)

    # return user_language, english_question
    print(f"User Language: {user_language}\nEnglish Question: {english_question}")

    # 2- Bot Answer
    answer = RasaChatbot().response(english_question)

    # 2.2- Assert the Answer in User Language
    answer_user_language = assert_user_language(user_language, answer)
    print(f"Bot: {answer_user_language}")

    # 3- Text To Speech Answer (text to audio file)
    audio_path = AzureTextToSpeech(answer_user_language, speak=False).synthesize()
    print(audio_path)

    # 4- Agent Video Responding to the question
    Wav2LipDiscriminator(audio_path=audio_path)

    response = f"Your Question: {question}\nAnswer: {answer_user_language}"
    return response


if __name__ == "__main__":
    live = True

    if live:
        print(main())
    else:
        path = "utils/audio_samples/audio1.wav"
        main(path)
