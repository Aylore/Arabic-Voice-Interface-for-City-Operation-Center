import azure.cognitiveservices.speech as speechsdk
from src.speechtotext.base import SpeechToText
import os


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
        speech_recognizer = speechsdk.SpeechRecognizer(
            speech_config=self.speech_config,
            auto_detect_source_language_config=self.auto_detect_source_language_config,
            audio_config=audio_config,
            )

        return speech_recognizer

    def postprocess(self, speech_recognizer):
        if self.live:
            print("--Start Talking---")
        else:
            print('--Record Uploaded--')

        result = speech_recognizer.recognize_once()

        # returning results
        if self.live:
            if result.reason == speechsdk.ResultReason.RecognizedSpeech:
                print("Text generated")
                return result.text
        else:
            if result.reason == speechsdk.ResultReason.RecognizedSpeech:
                print("Text generated")
                return result.text
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
        speech_recognizer = self.preprocess()
        transcripton = self.postprocess(speech_recognizer)
        return transcripton


if __name__ == "__main__":
    # print(AzureSpeechToText().transcribe())
    path = "utils/audio_samples/audio1.wav"
    print(AzureSpeechToText(path=path).transcribe())
