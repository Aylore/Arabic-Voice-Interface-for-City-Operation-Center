import azure.cognitiveservices.speech as speechsdk
import os
from utils.detect_language import LanguageDetector
from src.texttospeech.base import TextToSpeech


class AzureTextToSpeech(TextToSpeech):
    def __init__(
        self,
        text,
        speech_synthesis_language="ar-EG",
        speech_synthesis_voice_name="ar-EG-SalmaNeural",
        output_file=None,
    ):
        self.__speech_key, self.__service_region = os.getenv("AZURE_KEY"), "eastus"
        self.text = text
        self.output_file = output_file

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

        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
        return speech_synthesizer

    def postprocess(self, speech_synthesizer):
        result = speech_synthesizer.speak_text_async(self.text).get()
        return result

    def save_file(self, result):
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            audio_data = result.audio_data
            with open(output_file, "wb") as file:
                file.write(audio_data)
            print("Speech synthesized successfully. Audio saved to:", output_file)
        else:
            print("Speech synthesis failed:", result.reason)

    def read_aloud(self):
        speech_synthesizer = self.preprocess()
        result = self.postprocess(speech_synthesizer)
        return result


if __name__ == "__main__":
    # Create an instance of the AzureTextToSpeech class
    arabic_input_text = "اهلا انا سلمى كيف يمكنني مساعدتك"
    english_input_text = "Hello, My name is Jenny. How may I help you?"

    tts_arabic = AzureTextToSpeech(arabic_input_text).read_aloud()
    tts_english = AzureTextToSpeech(english_input_text).read_aloud()

    # # Provide the Arabic text you want to convert to speech
    # input_text = "اهلا انا سلمى كيف يمكنني مساعدتك"

    # # Specify the output file path
    # output_file_path = "output.wav"

    # # Synthesize speech and save the output to the file
    # tts.synthesize_speech(input_text, output_file_path)
