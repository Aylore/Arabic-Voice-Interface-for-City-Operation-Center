from utils.google_model.google_speech_to_text import GoogleSpeechToText

stt = GoogleSpeechToText()

def predict(path=None, audio_data=None, record=False):

    if record:
        stt.record_to_file(path)

    transcript = stt.transcribe_speech(audio_file_path = path, audio_data = audio_data)
    ## Note: Arabic is returned Reversed
    return transcript


# print(predict('utils/audio_samples/audio1.wav'))

