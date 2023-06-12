import azure.cognitiveservices.speech as speechsdk
import os


class AzureTextToSpeech:
    def __init__(self):
        self.__speech_key, self.__service_region = os.getenv("AZURE_KEY"), "eastus"

    def synthesize_speech(self, text, output_file=None):
        speech_config = speechsdk.SpeechConfig(
            subscription=self.__speech_key, region=self.__service_region
        )

        speech_config.speech_synthesis_language = "ar-EG"  # Arabic language
        speech_config.speech_synthesis_voice_name = "ar-EG-ShakirNeural"  # Arabic voice

        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

        result = speech_synthesizer.speak_text_async(text).get()

        # if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        #     audio_data = result.audio_data
        #     with open(output_file, "wb") as file:
        #         file.write(audio_data)

        #     print("Speech synthesized successfully. Audio saved to:", output_file)
        # else:
        #     print("Speech synthesis failed:", result.reason)


    # def to_speech



if __name__ == '__main__':
    # Create an instance of the AzureTextToSpeech class
    tts = AzureTextToSpeech()

    # Provide the Arabic text you want to convert to speech
    input_text = "اهلا انا شاكر، كيف يمكنني مساعدتك"

    # Specify the output file path
    output_file_path = "output.wav"

    # Synthesize speech and save the output to the file
    tts.synthesize_speech(input_text, output_file_path)
