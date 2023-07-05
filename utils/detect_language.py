"""

    This module provides a language detection utility using the Google Cloud Translation API.

    Classes:
    - LanguageDetector: Detects the language of a given text using the Google Cloud Translation API.
    - LanguageDetection: Represents the result of a language detection operation.

    Usage:
    - Import the module: import language_detection_utils
    - Create an instance of the LanguageDetector class.
    - Use the detect_language method to detect the language of a text:
    - detection = language_detector.detect_language(text)
    - Access the detected language, confidence score, and original text from the LanguageDetection object:
    - detected_language = detection.language
    - confidence_score = detection.confidence
    - original_text = detection.text

    Note:
    - The module requires the 'google.cloud.translate_v2' module to be imported.
    - The 'LanguageDetector' class uses the Google Cloud Translation API to detect the language.
    - The 'detect_language' method returns a 'LanguageDetection' object containing the detected language, confidence score, and original text.
    - The 'LanguageDetection' class represents the result of a language detection operation and provides properties to access the language, confidence score, and original text.
    - The 'GOOGLE_APPLICATION_CREDENTIALS' environment variable must be set to the path of the Google Cloud Translation API key file.


"""




from google.cloud import translate_v2 as translate
import os


class LanguageDetector:
    def __init__(self):
        os.environ[
            "GOOGLE_APPLICATION_CREDENTIALS"
        ] = "utils/google_model/google_secret_key.json"
        self.translate_client = translate.Client()

    def detect_language(self, text):
        """
            Text : the text you want to detect its langauge
            -returns
                the language of the text

        """
        result = self.translate_client.detect_language(text)

        detection = LanguageDetection(text, result["confidence"], result["language"])
        return detection


class LanguageDetection:
    def __init__(self, text, confidence, language):
        self.text = text
        self.confidence = confidence
        self.language = language


if __name__ == "__main__":
    text_to_detect = "Hello, how are you?"

    detector = LanguageDetector()
    detection = detector.detect_language(text_to_detect)

    print("Text: {}".format(detection.text))
    print("Confidence: {}".format(detection.confidence))
    print("Language: {}".format(detection.language))
