import azure.cognitiveservices.speech as speechsdk
import os

# Model class
class Azure_stt_model:
    """A model that taker audio path and returns text"""
    
    def __init__(self):
        # Set up the subscription info for the Speech Service:
        self.__speech_key, self.__service_region = os.getenv('AZURE_KEY'), "eastus"
        
        # Create an instance of a speech config with specified subscription key and service region.
        self.speech_config = speechsdk.SpeechConfig(subscription=self.__speech_key, region=self.__service_region)
        
        # identifying the language in an audio source 
        self.auto_detect_source_language_config = speechsdk.languageconfig.AutoDetectSourceLanguageConfig(languages=["en-US", "ar-EG"])
        
    def predict(self, path: str) -> str:
        """path: Path to audio file"""
        
        # recognize speech from an audio file
        audio_config = speechsdk.audio.AudioConfig(filename=path)

        # Create a recognizer with the given settings.
        speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=self.speech_config, 
        auto_detect_source_language_config=self.auto_detect_source_language_config, 
        audio_config=audio_config)
        
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