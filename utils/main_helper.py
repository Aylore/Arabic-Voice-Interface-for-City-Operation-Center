from utils.detect_language import LanguageDetector
from src.translation.azure_translator import AzureTranslator
from src.translation.google_translator import GoogleTranslator
from utils.word2num import words_to_numbers

def assert_english(question):
    detected_language = LanguageDetector().detect_language(question).language
    question = question.lower()
    if detected_language != "en":
        question = GoogleTranslator().translate(question).lower()
        question = words_to_numbers(question)
    return detected_language, question

def assert_user_language(detected_language, answer):
    if detected_language != "en":
        answer = GoogleTranslator().translate(answer).lower()
        answer = words_to_numbers(answer)
    return answer