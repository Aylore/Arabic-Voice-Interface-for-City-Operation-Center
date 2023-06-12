from utils.record_audio import AudioRecorder
from src.speechtotext.base import Sp
import os
from google.cloud import speech_v1p1beta1 as speech


# class SpeechToText:
#     def transcribe_speech(self, audio_file_path):
#         raise NotImplementedError("Subclasses must implement transcribe_speech method")


class GoogleSpeechToText(SpeechToText):
    def __init__(self, google_api_key=None, audio_file_path=None, audio_data=None):
        self.google_api_key = google_api_key

        # You will need the absolute path to be properly used when running django server
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] =  '/Users/aleedo/Coding/ITI/9-Months/Final Project/Arabic-Voice-Interface-for-City-Operation-Center/utils/google_model/google_secret_key.json'

        self.audio_file_path = audio_file_path
        self.audio_data = audio_data

    def preprocess(self):
        client = speech.SpeechClient()

        # Read the audio file
        if not self.audio_data:
            with open(self.audio_file_path, "rb") as audio_file:
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
    google_api_key = os.environ.get("GOOGLE_API")
    speech_to_text = GoogleSpeechToText(google_api_key)

    audio_file_path = "dataset/samples/sample_2.wav"
    speech_to_text.transcribe_speech(audio_file_path)
