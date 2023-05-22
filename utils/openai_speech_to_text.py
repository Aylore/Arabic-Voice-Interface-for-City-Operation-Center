import os
import openai


my_key = "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"

# Load your API key from an environment variable or secret management service
openai.api_key = my_key


audio_file= open("dataset/samples/sample_1.wav", "rb")

transcript = openai.Audio.transcribe("whisper-1", audio_file)