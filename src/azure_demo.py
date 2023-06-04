from utils.record_audio import AudioRecorder
from utils.azure_models.azure_speech_to_text import Azure_stt_model

# define path
path = "utils\audio_samples\audio1.wav"


def predict_live():
    live_transcript = Azure_stt_model().predict_live()
    return live_transcript

def demo():
    # record a voice
    recorder = AudioRecorder()
    print("Please speak a word into the microphone")
    # recorder.record_to_file(path = path)
    print(f"Done - result written to {path}")

    # get text from audio
    stt = Azure_stt_model()

    text = stt.predict(path)

    # printing (inversed to be shown in terminal)
    print(f"Text in audio: {text}")

if __name__ == '__main__':
    predict_live()

