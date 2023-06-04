from utils.azure_translator import Translator

# Example usage:
translator = Translator()
input_text1 = "I love english"
input_text2 = "انا احب العربية"

translated_text1 = translator.translate_text(input_text1)
translated_text2 = translator.translate_text(input_text2)

print(f"Original text: {input_text1}, Translated Text:", translated_text1)
print(f"Original text: {input_text2}, Translated Text:", translated_text2)

if __name__ == '__main__':
    # Example usage:
    translator = Translator()
    input_text1 = "I love english"
    input_text2 = "انا احب العربية"

    translated_text1 = translator.translate_text(input_text1)
    translated_text2 = translator.translate_text(input_text2)

    print(f"Original text: {input_text1}, Translated Text:", translated_text1)
    print(f"Original text: {input_text2}, Translated Text:", translated_text2)

