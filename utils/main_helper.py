
"""

This module provides utility functions for asserting and handling language in a question-and-answer system.

Functions:

  - Note:
    - The function uses the LanguageDetector class from the 'detect_language' module to detect the language of the question.
    - If the detected language is not English, the function translates the question using the GoogleTranslator class from the 'google_translator' module.
    - The function also applies the words_to_numbers function from the 'word2num' module to convert numbers in words to numeric form.
    - If the detected language is not English, the function translates the answer using the GoogleTranslator class from the 'google_translator' module.
    - The function also applies the words_to_numbers function from the 'word2num' module to convert numbers in words to numeric form.

"""




from utils.detect_language import LanguageDetector
from src.translation.azure_translator import AzureTranslator
from src.translation.google_translator import GoogleTranslator
from utils.word2num import words_to_numbers

def assert_english(question):
    """
      - assert_english(question): Asserts that the question is in English and performs necessary language processing if it is not.
      - Parameters:
        - question (str): The input question.
      - Returns:
        - detected_language (str): The detected language of the question.
        - processed_question (str): The processed question in English.
    """
    detected_language = LanguageDetector().detect_language(question).language
    question = question.lower()
    if detected_language != "en":
        question = GoogleTranslator().translate(question).lower()
        question = words_to_numbers(question)
    return detected_language, question

def assert_user_language(detected_language, answer):
    """
      - assert_user_language(detected_language, answer): Asserts the language of the user's answer and performs necessary language processing if it is not in English.
      - Parameters:
        - detected_language (str): The detected language of the user's question.
        - answer (str): The user's answer.
      - Returns:
        - processed_answer (str): The processed answer in English.
    """
    if detected_language != "en":
        answer = GoogleTranslator().translate(answer).lower()
        answer = words_to_numbers(answer)
    return answer