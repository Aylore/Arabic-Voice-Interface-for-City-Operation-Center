from google.cloud import translate_v2 as translate
import os


class TextTranslator:
    def __init__(self):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'utils/google_model/google_secret_key.json'
        self.translate_client = translate.Client()

    def translate(self, target, text):
        if isinstance(text, bytes):
            text = text.decode("utf-8")

        result = self.translate_client.translate(text, target_language=target)

        translation = Translation(result["input"], result["translatedText"], result["detectedSourceLanguage"])
        return translation


class Translation:
    def __init__(self, input_text, translated_text, detected_source_language):
        self.input_text = input_text
        self.translated_text = translated_text
        self.detected_source_language = detected_source_language



target_language = "ar-EG"   ## [ar-EG , en-US]
text_to_translate = "Hello, how are you?"

translator = TextTranslator()
translation = translator.translate(target_language, text_to_translate)

print("Text: {}".format(translation.input_text))
print("Translation: {}".format(translation.translated_text))
print("Detected source language: {}".format(translation.detected_source_language))

