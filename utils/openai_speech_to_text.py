import os
import openai


my_key = os.environ.get("OPENAI_KEY")

# Load your API key from an environment variable or secret management service
openai.api_key = my_key

audio_file= open("utils/audio_smaples/audio1.wav", "rb")


transcript = openai.Audio.transcribe("whisper-1", audio_file)