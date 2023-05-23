
def detect_lang(text):
    """Detects the text's language."""
    from google.cloud import translate_v2 as translate
    import os
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'utils/google_model/google_secret_key.json'

    translate_client = translate.Client()

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.detect_language(text)

    print(f"Text: {text}")
    print("Confidence: {}".format(result["confidence"]))
    print("Language: {}".format(result["language"]))



