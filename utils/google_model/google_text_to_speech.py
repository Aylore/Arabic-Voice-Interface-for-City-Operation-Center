from google.cloud import texttospeech
import os 


class GoogleTextToSpeech:
    def __init__(self) -> None:
        os.environ[
            "GOOGLE_APPLICATION_CREDENTIALS"
        ] = 'utils/google_model/google_secret_key.json'
        self.client =  texttospeech.TextToSpeechClient()


    def synthesize_speech(self, text, language_code):
        # Instantiates a client

        # Set the text input to be synthesized
        synthesis_input = texttospeech.SynthesisInput(text=text)

        # Build the voice request
        voice = texttospeech.VoiceSelectionParams(
            language_code=language_code,
            ssml_gender= texttospeech.SsmlVoiceGender.NEUTRAL,
        )

        # Select the type of audio file you want returned
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16
        )

        # Perform the text-to-speech request
        response = self.client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        # Write the response to the output file
        with open("dataset/google_tts/output.wav", "wb") as out:
            out.write(response.audio_content)
            print(f'Audio content written to file ')
