"""
    Module: text_matching

    This module provides a class for finding the best matching text from a given input using fuzzy string matching.

    Classes:
    - TextMatcher: Class for finding the best matching text based on input using fuzzy string matching.

 
    Usage:
    - Import the module: import text_matching
    - Create an instance of the TextMatcher class:
    - matcher = text_matching.TextMatcher(api_endpoint)
        - Parameters:
        - api_endpoint (str): The key to access the list of texts to match against. It should be one of the available keys in the 'data' dictionary.
    - Use the instance to find the best matching text:
    - best_match = matcher.find_best_match(input_text)
        - Parameters:
        - input_text (str): The input text to find the best match for.
        - Returns:
        - str: The closest matching text based on fuzzy string matching.

  
    Note:
    - The module requires the 'numpy' and 'fuzzywuzzy' libraries to be installed.
    - The 'data' dictionary contains the available texts to match against. It should be modified accordingly.
    - The 'find_best_match' function utilizes fuzzy string matching to calculate the similarity ratio between the input text and the available texts. It uses the 'fuzz.ratio' function from the 'fuzzywuzzy' library.
    - The 'find_best_match' function returns the closest matching text based on the highest similarity ratio.

"""


import numpy as np
from fuzzywuzzy import fuzz

data = {
    "by_domain_name": ["Water Management", "Energy Management", "Security Management"],
    "domain_count": ["Piston Car", "Cleaning Car", "Security Vehicles", "Parent Domain"]
}

class TextMatcher:
    def __init__(self, api_endpoint: str):
        """
        Initializes a TextMatcher instance.

        Args:
            api_endpoint: The name of the API endpoint that corresponds to the list of texts to match against.
        """
        self.api_endpoint = api_endpoint

    def find_best_match(self, input_text: str) -> str:
        """
        Finds the closest matching text in the list of texts associated with the TextMatcher instance.

        Args:
            input_text: The text to match against the list of texts.

        Returns:
            The closest matching text in the list of texts.
        """
        self.text_list = data[self.api_endpoint]
        distances = np.zeros(len(self.text_list))

        for i, text in enumerate(self.text_list):
            distances[i] = fuzz.ratio(input_text, text)  # Calculate the similarity ratio between input_text and each text in the list

        closest_index = np.argmax(distances)  # Find the index of the text with the highest similarity ratio
        closest_text = self.text_list[closest_index]  # Get the closest matching text based on the index

        return closest_text

if __name__ == "__main__":
    input_text = 'watar mangement'  # Typo: should match with 'Water Management'
    matcher = TextMatcher(api_endpoint="domain_count")
    best_match = matcher.find_best_match(input_text)
    print(f"The best match to '{input_text}' is '{best_match}'.")