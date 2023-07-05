"""
    This module provides a GoogleSpeechToText class for converting speech to text using the Google Cloud Speech-to-Text API.

    Classes:
    - GoogleSpeechToText: A speech-to-text class that uses the Google Cloud Speech-to-Text API for converting speech to text.

        Methods:
        - __init__(self, path: str = None, audio_data=None): Initializes the GoogleSpeechToText class by setting up the necessary credentials and input options.
        - preprocess(self): Preprocesses the speech recognition by configuring the speech recognition request.
        - postprocess(self, response): Processes the speech recognition response and returns the transcript.
        - transcribe(self): Performs the speech-to-text conversion and returns the transcribed text.


"""


from utils.record_audio import AudioRecorder
from src.speechtotext.base import SpeechToText
import os
from google.cloud import speech_v1p1beta1 as speech


# class SpeechToText:
#     def transcribe_speech(self, path):
#         raise NotImplementedError("Subclasses must implement transcribe_speech method")


class GoogleSpeechToText(SpeechToText):
    def __init__(self, path: str = None, audio_data=None):
        self.google_api_key = os.environ.get("GOOGLE_API")

        # You will need the absolute path to be properly used when running django server
        os.environ[
            "GOOGLE_APPLICATION_CREDENTIALS"
        ] = "utils/google_model/google_secret_key.json"

        self.path = path
        self.audio_data = audio_data

    def preprocess(self):
        client = speech.SpeechClient()

        # Read the audio file
        if not self.audio_data:
            with open(self.path, "rb") as audio_file:
                self.audio_data = audio_file.read()

        # Configure speech recognition request
        audio = speech.RecognitionAudio(content=self.audio_data)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            language_code="ar-EG",
            alternative_language_codes=["en-US"],
        )

        # Perform speech recognition
        response = client.recognize(config=config, audio=audio)
        return response

    def postprocess(self, response):
        # Process the response
        for result in response.results:
            print("Transcript: {}".format(result.alternatives[0].transcript[::-1]))
            return result.alternatives[0].transcript[::-1]

    def transcribe(self):
        response = self.preprocess()
        transcripton = self.postprocess(response)
        return transcripton


if __name__ == "__main__":
    path = "utils/audio_samples/audio1.wav"
    GoogleSpeechToText(path=path).transcribe()
