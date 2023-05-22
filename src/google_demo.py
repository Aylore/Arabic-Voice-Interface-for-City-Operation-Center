from utils.google_model.google_speech_to_text import GoogleSpeechToText 

stt = GoogleSpeechToText()


stt.record_to_file("dataset/samples/sample_5.wav")


stt.transcribe_speech("dataset/samples/sample_2.wav")