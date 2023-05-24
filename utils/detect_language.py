from google.cloud import translate_v2 as translate
import os


class LanguageDetector:
    def __init__(self):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'utils/google_model/google_secret_key.json'
        self.translate_client = translate.Client()

    def detect_language(self, text):
        result = self.translate_client.detect_language(text)

        detection = LanguageDetection(text, result["confidence"], result["language"])
        return detection


class LanguageDetection:
    def __init__(self, text, confidence, language):
        self.text = text
        self.confidence = confidence
        self.language = language


# text_to_detect = "Hello, how are you?"

# detector = LanguageDetector()
# detection = detector.detect_language(text_to_detect)

# print("Text: {}".format(detection.text))
# print("Confidence: {}".format(detection.confidence))
# print("Language: {}".format(detection.language))
