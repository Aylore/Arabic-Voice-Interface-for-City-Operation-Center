from google.cloud import translate_v2 as translate
import os
from src.translation.base import Translator


class GoogleTranslator(Translator):
    def __init__(self, text, target):
        os.environ[
            "GOOGLE_APPLICATION_CREDENTIALS"
        ] = "utils/google_model/google_secret_key.json"
        self.translate_client = translate.Client()
        self.text = text
        self.target = target

    def preprocess(self):
        if isinstance(self.text, bytes):
            self.text = self.text.decode("utf-8")

        response = self.translate_client.translate(
            self.text, target_language=self.target
        )
        return response

    def postprocess(self, response):
        translation = Translation(
            response["input"],
            response["translatedText"],
            response["detectedSourceLanguage"],
        )
        return translation

    def __translate(self):
        response = self.preprocess()
        translation = self.postprocess(response)
        return translation

    def translate(self):
        return self.__translate().translated_text


class Translation:
    def __init__(self, input_text, translated_text, detected_source_language):
        self.input_text = input_text
        self.translated_text = translated_text
        self.detected_source_language = detected_source_language


if __name__ == "__main__":
    target_language = "ar-EG"  ## [ar-EG , en-US]
    text_to_translate = "Hello, how are you?"

    translator = GoogleTranslator(text_to_translate, target_language)
    translation = translator.translate()
    print("Translation: {}".format(translation))

    # translation = translate.__translate()
    # # print("Text: {}".format(translation.input_text))
    # # print("Translation: {}".format(translation.translated_text))
    # # print("Detected source language: {}".format(translation.detected_source_language))
