from utils.detect_language import LanguageDetector
from src.translation.azure_translator import AzureTranslator

def assert_english(question):
    detected_language = LanguageDetector().detect_language(question).language
    if detected_language != "en":
        question = AzureTranslator().translate(question)
    return detected_language, question

def assert_user_language(detected_language, answer):
    if detected_language != "en":
        answer = AzureTranslator().translate(answer)
    return answer