import requests
import uuid
from langdetect import detect
import os

class Translator:
    def __init__(self):
        self.key = os.environ['azure_trans_key']
        self.location = "eastus"
        self.endpoint = "https://api.cognitive.microsofttranslator.com"
        self.path = '/translate'
        self.constructed_url = self.endpoint + self.path
        self.headers = {
            'Ocp-Apim-Subscription-Key': self.key,
            'Ocp-Apim-Subscription-Region': self.location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

    def translate_text(self, text):
        language = detect(text)
        if language == 'ar':
            self.from_lang, self.to_lang = "ar", "en"
        else :
            self.from_lang, self.to_lang = "en", "ar"
            
        params = {
            'api-version': '3.0',
            'from': self.from_lang,
            'to': self.to_lang
        }

        body = [{'text': text}]

        response = requests.post(self.constructed_url, params=params, headers=self.headers, json=body)
        response_data = response.json()
        translated_text = response_data[0]['translations'][0]['text']

        return translated_text