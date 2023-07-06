"""
This is the main module of the project which contains the pipeline of the chatbot that can answer user questions and generate video responses to those questions.
The pipeline includes several steps, including speech-to-text transcription, language assertion, response generation using Rasa, text-to-speech synthesis, and Lip-syncing using SOTA Wav2lip
"""

import logging
import datetime
from typing import Tuple
from utils.main_helper import assert_english, assert_user_language

from src.speechtotext.google_speech_to_text import GoogleSpeechToText
from src.speechtotext.azure_speech_to_text import AzureSpeechToText

from src.texttospeech.google_text_to_speech import GoogleTextToSpeech
from src.texttospeech.azure_text_to_speech import AzureTextToSpeech

from src.rasa.rasamodel import RasaChatbot
from src.wav2lip.inference import main as Wav2LipDiscriminator
from src.wav2lip.face_restoration.video_enhance import main as EnhanceVideo


def log_step(logger: logging.Logger, step_name: str, start_time: datetime.datetime) -> datetime.datetime:    
    """
    Logs the elapsed time for a pipeline step.

    Args:
        logger: The logger object to use for logging.
        step_name: The name of the pipeline step being logged.
        start_time: The start time of the pipeline step.

    Returns:
        The end time of the pipeline step.
    """
    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    logger.info(f"{step_name}: {elapsed_time}")
    return end_time


def main(path: str = None, enhance: bool = True) -> Tuple[str, bool]:
    """
    Runs the pipeline.

    1. Speech To Text

        The first step of the pipeline is to transcribe the user's spoken question into text using a speech-to-text system. We use the Azure Speech Services API to perform this task. If an audio file path is provided, we use the Azure Speech SDK to transcribe the audio. If no audio file path is provided, we use the microphone on the user's device to capture their spoken question and transcribe it in real-time.

    2. Assert Language and Translate

        Once we have the user's question in text form, we assert that the text is in English. If it is not, we translate the text into English using the Google Translate API. This step ensures that the chatbot can process the user's question correctly.

    3. Process Question with Chatbot

        After the user's question has been transcribed and translated (if necessary), we process it using a chatbot. We use the Rasa framework to implement the chatbot. The chatbot generates a response to the user's question based on the intent and entities identified in the question.

    4. Translate and Synthesize Response

        Once we have the chatbot's response in English, we translate it into the user's language (if necessary) using the Google Translate API. We then use the Azure Speech SDK to synthesize the response into an audio file. The audio file can be played back to the user as the chatbot's spoken response.

    5. Generate Video Response

        Finally, we generate a video response to the user's question using the Wav2Lip model. The Wav2Lip model takes the synthesized audio file and generates a video of an agent speaking the response. If the `enhance` flag is set to `True`, we enhance the video using a neural network-based video enhancer (Code Former).

    Args:
        path: Optional. The path to an audio file containing the user's question.
        enhance: Optional. Whether to enhance the generated video response.

    Returns:
        1- A string containing the user's question and the chatbot's response.
        2- Whether to enhance the generated video response.
    """
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # 1- Speech to Text (getting the client question)
    start_time_question = datetime.datetime.now()
    question = AzureSpeechToText(path).transcribe()
    logger.info(f"User: {question}")

    # 1.1 - Assert the question in English For the chatbot
    start_time_assert_english = log_step(
        logger, "Speech to Text Time", start_time_question
    )
    user_language, english_question = assert_english(question)
    logger.info(f"User Language: {user_language}, English Question: {english_question}")

    # 2- Bot Answer
    start_time_answer = log_step(
        logger, "Assert Question in English Time", start_time_assert_english
    )
    answer = RasaChatbot().response(english_question)
    logger.info(f"Bot: {answer}")

    # 2.2- Assert the Answer in User Language
    start_time_assert_user_language = log_step(
        logger, "Bot Response Time", start_time_answer
    )
    answer_user_language = assert_user_language(user_language, answer)
    logger.info(f"Answer User Language: {answer_user_language}")

    # 3- Text To Speech Answer (text to audio file)
    start_time_tts = log_step(
        logger, "Assert Answer in User Language Time", start_time_assert_user_language
    )
    AzureTextToSpeech(answer_user_language, speak=False).synthesize()

    # 4- Agent Video Responding to the question
    start_time_wav2lip = log_step(logger, "Text to Speech Time", start_time_tts)
    Wav2LipDiscriminator()

    # 5- Enhance Wav2lip Discriminator Output
    if enhance:
        start_time_enhance = log_step(
            logger, "Agent Video Response Time", start_time_wav2lip
        )
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