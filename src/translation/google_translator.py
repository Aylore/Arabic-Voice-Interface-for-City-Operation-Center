"""
    This module provides a GoogleTranslator class for translating text using the Google Cloud Translation API.

    Classes:
    - GoogleTranslator: A translator class that uses the Google Cloud Translation API for text translation.

        Methods:
        - __init__(): Initializes the GoogleTranslator class by setting up the Google Cloud Translation client.
        - preprocess(text): Preprocesses the text for translation, including language detection and target language selection.
        - postprocess(response): Postprocesses the translation response and returns a Translation object.
        - __translate(text): Private method that performs the translation process.
        - translate(text): Translates the given text and returns the translated text.
        
    - Translation: A class representing a translation result.

        Attributes:
        - input_text: The input text to be translated.
        - translated_text: The translated text.
        - detected_source_language: The detected source language of the input text.
"""


import os
from const import GOOGLE_SECRET_KEY
from google.cloud import translate_v2 as translate
from src.translation.base import Translator
from utils.detect_language import LanguageDetector


class GoogleTranslator(Translator):
    def __init__(self):
        os.environ[
            "GOOGLE_APPLICATION_CREDENTIALS"
        ] = GOOGLE_SECRET_KEY
        self.translate_client = translate.Client()

    def preprocess(self, text):
        text = text.lower()

        if isinstance(text, bytes):
            text = text.decode("utf-8")

        detected_language = LanguageDetector().detect_language(text).language
        target = "ar-EG" if detected_language == "en" else "en-US"

        response = self.translate_client.translate(text, target_language=target)
        return response

    def postprocess(self, response):
        translation = Translation(
            response["input"],
            response["translatedText"],
            response["detectedSourceLanguage"],
        )
        return translation

    def __translate(self, text):
        response = self.preprocess(text)
        translation = self.postprocess(response)
        return translation

    def translate(self, text):
        return self.__translate(text).translated_text


class Translation:
    def __init__(self, input_text, translated_text, detected_source_language):
        self.input_text = input_text
        self.translated_text = translated_text
        self.detected_source_language = detected_source_language


if __name__ == "__main__":
    # if detected_language == "en":
    # target_language = "ar-EG"  ## [ar-EG , en-US]
    text_to_translate = "Domain ID for the alert id 3"

    with open("src/rasa/data/example-english.txt", "r") as f:
        text_to_translate = f.read()
    # else:
    # target_language = "en-US"
    # text_to_translate = "معرف النطاق لمعرف التنبيه 3"

    translator = GoogleTranslator()
    translation = translator.translate(text_to_translate)

    with open("src/rasa/data/google_example-arabic.txt", "w") as f:
        f.write(translation)

    # print("Translation: {}".format(translation))

    with open("src/rasa/data/google_example-arabic.txt", "r") as f:
        text_to_translate = f.read()

    translator = GoogleTranslator()
    translation = translator.translate(text_to_translate)
    # print(translation)

    with open("src/rasa/data/google-example-english-after-arabic.txt", "w") as f:
        f.write(translation)

    # translation = translate.__translate()
    # print("Text: {}".format(translation.input_text))
    # print("Translation: {}".format(translation.translated_text))
    # print("Detected source language: {}".format(translation.detected_source_language))
