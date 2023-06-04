from utils.google_model.google_text_to_speech import GoogleTextToSpeech
from utils.detect_language import LanguageDetector


tts = GoogleTextToSpeech()

# Set the text and other parameters
text = "مرحبا جميعا كيف حالكم"
language_code = "ar-EG"   ##  ar-EG    ---    en-US

ld = LanguageDetector()



def get_tts(text =text ):


    detected_lang = ld.detect_language(text )
    if detected_lang.language == "ar":
        language_code = "ar-EG"
    elif detected_lang.language == "en":
        language_code = "en-US"

    print(f"detected language is {detected_lang.language} with confidence : {detected_lang.confidence}")
    # Use the interface to synthesize speech
    tts.synthesize_speech(text, language_code)






# get_tts(text)
