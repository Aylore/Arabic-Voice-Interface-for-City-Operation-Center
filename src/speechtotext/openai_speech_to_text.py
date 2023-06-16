import os
import openai


class OpenAISpeechToText:
    def __init__(self, file_path):
        # Load your API key from an environment variable or secret management service
        self.key = os.environ.get("OPENAI_KEY")
        self.file_path = file_path

    def preprocess(self):
        audio_file = open(self.file_path, "rb")
        return audio_file

    def postprocess(self, audio_file):
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return transcript

    def transcribe(self):
        audio_file = self.preprocess()
        transcript = self.postprocess(audio_file)
        return transcript


if __name__ == '__main__':
    file_path = "utils/audio_smaples/audio1.wav"
    print(OpenAISpeechToText(file_path).transcribe())

