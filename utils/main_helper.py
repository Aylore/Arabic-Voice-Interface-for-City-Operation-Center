
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

from typing import Tuple
from utils.detect_language import LanguageDetector
from src.translation.azure_translator import AzureTranslator
from src.translation.google_translator import GoogleTranslator
from utils.word2num import words_to_numbers

def assert_english(question: str) -> Tuple[str, str]:
    """
    Checks if a given text input is in English. If it's not in English, the function translates the input to English 
    and converts any words that represent numbers to their numerical values.

    Args:
        question: A string representing the input text.

    Returns:
        A tuple containing the detected language and the translated and converted input text.
    """
    detected_language = LanguageDetector().detect_language(question).language
    question = question.lower()
    if detected_language != "en":
        question = GoogleTranslator().translate(question).lower()
        question = words_to_numbers(question)
    return detected_language, question
    

def assert_user_language(detected_language: str, answer: str) -> str:
    """
    Translates a given answer to the detected language (if it's not in English) and converts any words that represent 
    numbers to their numerical values.

    Args:
        detected_language: A string representing the detected language of the input text.
        answer: A string representing the answer to translate and convert.

    Returns:
        A string representing the translated and converted answer.
    """
    if detected_language != "en":
        answer = GoogleTranslator().translate(answer).lower()
        answer = words_to_numbers(answer)
    return answer