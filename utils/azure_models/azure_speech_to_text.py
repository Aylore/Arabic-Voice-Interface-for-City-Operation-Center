import azure.cognitiveservices.speech as speechsdk
import os


# Model class
class Azure_stt_model:
    """A model that taker audio path and returns text"""

    def __init__(self):
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

    def predict(self, path: str) -> str:
        """path: Path to audio file"""

        # recognize speech from an audio file
        audio_config = speechsdk.audio.AudioConfig(filename=path)

        # Create a recognizer with the given settings.
        speech_recognizer = speechsdk.SpeechRecognizer(
            speech_config=self.speech_config,
            auto_detect_source_language_config=self.auto_detect_source_language_config,
            audio_config=audio_config,
        )

        # getting results
        result = speech_recognizer.recognize_once()

        # returning results
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Text generated")
            return result.text
        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(result.no_match_details))
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))

    def predict_live(self):
        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

        # Create a recognizer with the given settings.
        speech_recognizer = speechsdk.SpeechRecognizer(
            speech_config=self.speech_config,
            auto_detect_source_language_config=self.auto_detect_source_language_config,
            audio_config=audio_config,
        )

        # getting results
        print('--Start Talking---')
        result = speech_recognizer.recognize_once()
        # yield speech_recognizer.start_continuous_recognition()

        # # returning results
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Text generated")
            return result.text

        # speech_config = speechsdk.SpeechConfig(
        #     subscription=os.getenv("AZURE_KEY"), region="eastus"
        # )
        # audio_input = speechsdk.AudioConfig(use_default_microphone=True)

        # # Create a recognizer from the speech config and audio input
        # recognizer = speechsdk.SpeechRecognizer(
        #     speech_config=speech_config, audio_config=audio_input
        # )

        # # Start the recognizer and transcribe the audio in real-time
        # done = False

        # def stop_cb(evt):
        #     nonlocal done
        #     done = True

        # recognizer.recognized.connect(lambda evt: print("RECOGNIZED:", evt.result.text))

        # # recognizer.session_started.connect(lambda evt: print("SESSION STARTED"))
        # # recognizer.session_stopped.connect(lambda evt: print("SESSION STOPPED"))
        # # recognizer.canceled.connect(lambda evt: print("CANCELED:", evt.reason))
        # # recognizer.session_stopped.connect(stop_cb)
        # # recognizer.start_continuous_recognition()

        # # Continuously get the transcription and return it as a JSON response
        # # while not done:
        # #     result = recognizer.recognize_once()
        # #     if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        # #         transcript = result.text

        # return done

        # def stream():
        #     while not done:
        #         result = recognizer.recognize_once()
        #         if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        #             transcription = result.text
        #             yield f"data: {transcription}\n\n"
        #         # time.sleep(1)

        # stream()

if __name__ == '__main__':
    print(Azure_stt_model().predict_live())
