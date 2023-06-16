import numpy as np
from fuzzywuzzy import fuzz

data = {
    "by_domain_name": ["Water Management", "Energy Management", "Security Management"],
    "domain_count": ["Piston Car", "Cleaning Car", "Security Vehicles", "Parent Domain"]
}

class TextMatcher:
    def __init__(self, api_endpoint: str):
        self.api_endpoint = api_endpoint

    def find_best_match(self, input_text):
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