"""
    This module provides an AzureTranslator class for translating text using the Azure Cognitive Services Translator Text API.

    Classes:
    - AzureTranslator: A translator class that uses the Azure Cognitive Services Translator Text API for text translation.

        Methods:
        - __init__(): Initializes the AzureTranslator class by setting up the necessary credentials and endpoint.
        - preprocess(text): Preprocesses the text for translation, including language detection and language pair selection.
        - postprocess(response): Postprocesses the translation response and returns the translated text.
        - translate(text): Translates the given text and returns the translated text.

"""



import requests
import uuid
from langdetect import detect
import os
from src.translation.base import Translator


class AzureTranslator(Translator):
    def __init__(self):
        self.key = os.environ["azure_trans_key"]
        self.location = "eastus"
        self.endpoint = "https://api.cognitive.microsofttranslator.com"
        self.path = "/translate"
        self.constructed_url = self.endpoint + self.path
        self.headers = {
            "Ocp-Apim-Subscription-Key": self.key,
            "Ocp-Apim-Subscription-Region": self.location,
            "Content-type": "application/json",
            "X-ClientTraceId": str(uuid.uuid4()),
        }

    def preprocess(self, text):
        language = detect(text)
        if language == "ar":
            self.from_lang, self.to_lang = "ar", "en"
        else:
            self.from_lang, self.to_lang = "en", "ar"

        params = {"api-version": "3.0", "from": self.from_lang, "to": self.to_lang}

        body = [{"text": text}]

        response = requests.post(
            self.constructed_url, params=params, headers=self.headers, json=body
        )
        response = response.json()
        return response

    def postprocess(self, response):
        translated_text = response[0]["translations"][0]["text"]
        return translated_text

    def translate(self, text):
        response = self.preprocess(text)
        translation = self.postprocess(response)
        return translation


if __name__ == "__main__":
    # text_to_translate = "Hello, how are you?"

    with open("src/rasa/data/english-questions.txt", "r") as f:
        text_to_translate = f.read()

    translator = AzureTranslator()
    translation = translator.translate(text_to_translate)

    with open("src/rasa/data/azure-arabic-questions.txt", "w") as f:
        f.write(translation)

    # with open('src/rasa/data/example-arabic.txt', 'r') as f:
    #     text_to_translate = f.read()

    # translator = AzureTranslator()
    # translation = translator.translate(text_to_translate)

    # with open('src/rasa/data/azure-example-english-after-arabic.txt', 'w') as f:
    #     f.write(translation)

    # translation = translator.translate(text_to_translate)

    # print("Translation: {}".format(translation))
