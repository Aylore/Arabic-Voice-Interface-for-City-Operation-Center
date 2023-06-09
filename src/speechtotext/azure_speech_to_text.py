"""
        
    This module provides an AzureSpeechToText class for converting speech to text using the Azure Cognitive Services Speech-to-Text API.

    Classes:
    - AzureSpeechToText: A speech-to-text class that uses the Azure Cognitive Services Speech-to-Text API for converting speech to text.

        Methods:
        - __init__(self, path: str = None): Initializes the AzureSpeechToText class by setting up the necessary credentials and input options.
        - preprocess(self): Preprocesses the speech recognition by creating a recognizer with the given settings.
        - postprocess(self): Processes the speech recognition result and returns the transcribed text.
        - transcribe(self): Performs the speech-to-text conversion and returns the transcribed text.


"""


import azure.cognitiveservices.speech as speechsdk
from src.speechtotext.base import SpeechToText
import os
from utils.word2num import words_to_numbers


# Model class
class AzureSpeechToText(SpeechToText):
    """A model that taker audio path and returns text"""

    def __init__(self, path: str = None):
        # Set up the subscription info for the Speech Service:
        self.__speech_key, self.__service_region = os.getenv("AZURE_KEY"), "eastus"

        # Create an instance of a speech config with specified subscription key and service region.
        self.speech_config = speechsdk.SpeechConfig(
            subscription=self.__speech_key, region=self.__service_region
        )

        # Enable number parsing
        self.speech_config.output_format = speechsdk.OutputFormat.Simple

        # identifying the language in an audio source
        self.auto_detect_source_language_config = (
            speechsdk.languageconfig.AutoDetectSourceLanguageConfig(
                languages=["en-US", "ar-EG"]
            )
        )

        self.path = path
        self.live = False if self.path else True

    def preprocess(self) -> str:
        if self.live:
            audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        else:
            audio_config = speechsdk.audio.AudioConfig(filename=self.path)

        # Create a recognizer with the given settings.
        self.speech_recognizer = speechsdk.SpeechRecognizer(
            speech_config=self.speech_config,
            auto_detect_source_language_config=self.auto_detect_source_language_config,
            audio_config=audio_config,
        )

    def postprocess(self):
        if self.live:
            print("--Start Talking---")
        else:
            print("--Record Uploaded--")

        result = self.speech_recognizer.recognize_once()

        # Parse numbers using the NumberParser class and replace with integer values

        final_result = words_to_numbers(result.text.lower())

        # returning results
        if self.live:
            if result.reason == speechsdk.ResultReason.RecognizedSpeech:
                print("Text generated")
                return final_result
        else:
            if result.reason == speechsdk.ResultReason.RecognizedSpeech:
                print("Text generated")
                return final_result
            elif result.reason == speechsdk.ResultReason.NoMatch:
                print(
                    "No speech could be recognized: {}".format(result.no_match_details)
                )
            elif result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = result.cancellation_details
                print(
                    "Speech Recognition canceled: {}".format(
                        cancellation_details.reason
                    )
                )
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    print(
                        "Error details: {}".format(cancellation_details.error_details)
                    )

    def transcribe(self) -> str:
        self.preprocess()
        transcripton = self.postprocess()
        return transcripton


if __name__ == "__main__":
    live = True
    if live:
        print(AzureSpeechToText().transcribe())
    else:
        path = "utils/audio_samples/audio1.wav"
        print(AzureSpeechToText(path=path).transcribe())
