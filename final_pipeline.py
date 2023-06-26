from src.speechtotext.google_speech_to_text import GoogleSpeechToText
from src.speechtotext.azure_speech_to_text import AzureSpeechToText

from src.texttospeech.google_text_to_speech import GoogleTextToSpeech
from src.texttospeech.azure_text_to_speech import AzureTextToSpeech

from src.rasa.rasamodel import RasaChatbot
from utils.main_helper import assert_english, assert_user_language
from src.wav2lip.inference import main as Wav2LipDiscriminator
from src.wav2lip.face_restoration.video_enhance import main as EnhanceVideo

import logging
import datetime

def log_step(logger, step_name, start_time):
    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    logger.info(f"{step_name}: {elapsed_time}")
    return end_time

def main(path=None, enhance=False):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # 1- Speech to Text (getting the client question)
    start_time_question = datetime.datetime.now()
    question = AzureSpeechToText(path).transcribe()
    logger.info(f"User: {question}")
        
    # 1.1 - Assert the question in English For the chatbot
    start_time_assert_english = log_step(logger, "Speech to Text Time", start_time_question)
    user_language, english_question = assert_english(question)
    logger.info(f"User Language: {user_language}, English Question: {english_question}")

    # 2- Bot Answer
    start_time_answer = log_step(logger, "Assert Question in English Time", start_time_assert_english)
    answer = RasaChatbot().response(english_question)
    logger.info(f"Bot: {answer}")

    # 2.2- Assert the Answer in User Language
    start_time_assert_user_language = log_step(logger, "Bot Response Time", start_time_answer)
    answer_user_language = assert_user_language(user_language, answer)
    logger.info(f"Answer User Language: {answer_user_language}")

    # 3- Text To Speech Answer (text to audio file)
    start_time_tts = log_step(logger, "Assert Answer in User Language Time", start_time_assert_user_language)
    AzureTextToSpeech(answer_user_language, speak=False).synthesize()

    # 4- Agent Video Responding to the question
    start_time_wav2lip = log_step(logger, "Text to Speech Time", start_time_tts)
    Wav2LipDiscriminator()

    # 5- Enhance Wav2lip Discriminator Output
    if enhance:
        start_time_enhance = log_step(logger, "Agent Video Response Time", start_time_wav2lip)
        EnhanceVideo()
        end_time_pipeline = log_step(logger, "Enhance Video Time", start_time_enhance)

    full_time_pipeline = log_step(logger, "Full Pipeline Time", start_time_question)
    response = f"Your Question: {question}\nAnswer: {answer_user_language}"
    return response, enhance


if __name__ == "__main__":
    live = True

    if live:
        print(main())
    else:
        path = "utils/audio_samples/audio1.wav"
        main(path)
