"""
    This module provides an AzureTextToSpeech class for converting text to speech using the Azure Cognitive Services Text-to-Speech API.

    Classes:
    - AzureTextToSpeech: A text-to-speech class that uses the Azure Cognitive Services Text-to-Speech API for converting text to speech.

        Methods:
        - __init__(self, text, speak=True, speech_synthesis_language="ar-EG", speech_synthesis_voice_name="ar-EG-SalmaNeural", output_file="/Interface/google_app/static/answer.wav"): Initializes the AzureTextToSpeech class by setting up the necessary credentials and options.
        - preprocess(self): Preprocesses the text-to-speech conversion by setting up the speech configuration.
        - postprocess(self): Performs the text-to-speech conversion and returns the result.
        - save_file(self, result): Saves the synthesized speech audio to a file and returns the file path.
        - read_aloud(self): Performs the text-to-speech conversion and reads the synthesized speech aloud.
        - synthesize(self): Performs the text-to-speech conversion and saves the synthesized speech audio to a file.


"""


import os
from const import SYNTHESIZED_AUDIO
import azure.cognitiveservices.speech as speechsdk
from utils.detect_language import LanguageDetector
from src.texttospeech.base import TextToSpeech


class AzureTextToSpeech(TextToSpeech):
    def __init__(
        self,
        text,
        speak=True,
        speech_synthesis_language="ar-EG",
        speech_synthesis_voice_name="ar-EG-SalmaNeural",
        output_file=SYNTHESIZED_AUDIO,
    ):
        self.__speech_key, self.__service_region = os.getenv("AZURE_KEY"), "eastus"
        self.text = text
        self.output_file = output_file
        self.speak = speak
        self.language = LanguageDetector().detect_language(self.text).language

        if self.language == "en":
            self.speech_synthesis_language = "en-US"  # Arabic language
            self.speech_synthesis_voice_name = "en-US-JennyNeural"  # Arabic voice
        if self.language == "ar":
            self.speech_synthesis_language = "ar-EG"  # Arabic language
            self.speech_synthesis_voice_name = "ar-EG-SalmaNeural"

    def preprocess(self):
        speech_config = speechsdk.SpeechConfig(
            subscription=self.__speech_key, region=self.__service_region
        )

        speech_config.speech_synthesis_language = (
            self.speech_synthesis_language
        )  # Arabic language
        speech_config.speech_synthesis_voice_name = (
            self.speech_synthesis_voice_name
        )  # Arabic voice

        if not self.speak:
            audio_config = speechsdk.audio.PullAudioOutputStream()
            self.speech_synthesizer = speechsdk.SpeechSynthesizer(
                speech_config=speech_config, audio_config=audio_config
            )
        else:
            self.speech_synthesizer = speechsdk.SpeechSynthesizer(
                speech_config=speech_config,
            )

    def postprocess(self):
        result = self.speech_synthesizer.speak_text_async(self.text).get()
        return result

    def save_file(self, result):
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            audio_data = result.audio_data
            with open(self.output_file, "wb") as file:
                file.write(audio_data)
            return self.output_file
            print("Speech synthesized successfully. Audio saved to:", self.output_file)
        else:
            print("Speech synthesis failed:", result.reason)

    def read_aloud(self):
        self.preprocess()
        result = self.postprocess()
        return result

    def synthesize(self):
        self.preprocess()
        result = self.postprocess()
        audio_path = self.save_file(result)
        return audio_path


if __name__ == "__main__":
    # Create an instance of the AzureTextToSpeech class
    arabic_input_text = "اهلا انا سلمى كيف يمكنني مساعدتك"
    english_input_text = "Hello, My name is Jenny. How may I help you?"

    tts_arabic = AzureTextToSpeech(arabic_input_text).read_aloud()
    tts_english = AzureTextToSpeech(english_input_text).read_aloud()

    # To save an audio file of the given text
    print(AzureTextToSpeech(english_input_text, speak=False).synthesize())
