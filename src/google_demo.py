from utils.google_model.google_speech_to_text import GoogleSpeechToText 



def predict(path , record = False):
    stt = GoogleSpeechToText()
    if record:
        stt.record_to_file(path)


    return stt.transcribe_speech(path)


# predict("dataset/samples/sample_1.wav")