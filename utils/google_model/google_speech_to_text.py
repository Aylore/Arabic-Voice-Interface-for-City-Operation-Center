# import os 
# from google.cloud import speech_v1p1beta1 as speech
from utils.record_audio import AudioRecorder




# google_key = os.environ.get('GOOGLE_API')
# #setting Google credential
# os.environ['GOOGLE_APPLICATION_CREDENTIALS']= 'utils/google/google_secret_key.json'







# def transcribe_speech(audio_file_path , user_input = False):
#     client = speech.SpeechClient()
    

#     if user_input:

#         audio = AudioRecorder()
#         sample = audio.record_to_file("dataset/samples/sample_3.wav")
#         audio_file_path = "dataset/samples/sample_3.wav"
#     else :
#         audio_file_path = "dataset/samples/sample_2.wav"


#     # Read the audio file
#     with open(audio_file_path, "rb") as audio_file:
#         audio_data = audio_file.read()

#     # Configure speech recognition request
#     audio = speech.RecognitionAudio(content=audio_data)
#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        
#         language_code="ar-EG",
#         alternative_language_codes=["en-US"],


#     )

#     # Perform speech recognition
#     response = client.recognize(config=config, audio=audio)
#     # print(response.results)
#     # Process the response
#     for result in response.results:
#         # print("Words: {}".format(result.alternatives[0].words[0].word))

#         # print(f"First lang : {result}")

#         print("Transcript: {}".format(result.alternatives[0].transcript[::-1]))

# # Provide the path to your audio file
# # audio_file_path = "dataset/samples/sample_2.wav"

# # # Call the function to transcribe the speech
# # transcribe_speech(audio_file_path = audio_file_path)








#################################################################



import os
from google.cloud import speech_v1p1beta1 as speech


class SpeechToText:
    def transcribe_speech(self, audio_file_path):
        raise NotImplementedError("Subclasses must implement transcribe_speech method")


class GoogleSpeechToText(SpeechToText):
    def __init__(self, google_api_key=None):
        self.google_api_key = google_api_key
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'utils/google_model/google_secret_key.json'

    def transcribe_speech(self, audio_file_path):
        client = speech.SpeechClient()

        # Read the audio file
        with open(audio_file_path, "rb") as audio_file:
            audio_data = audio_file.read()

        # Configure speech recognition request
        audio = speech.RecognitionAudio(content=audio_data)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            language_code="ar-EG",
            alternative_language_codes=["en-US"],
        )

        # Perform speech recognition
        response = client.recognize(config=config, audio=audio)

        # Process the response
        for result in response.results:
            print("Transcript: {}".format(result.alternatives[0].transcript[::-1]))



    def record_to_file(self, file_path):
        """
            Input the path to save the record with the name of the record file 
        """

        # Code for recording audio and saving it to the specified file path
        
        audio = AudioRecorder()
        
        sample = audio.record_to_file(file_path)

      
        # audio_file_path = "dataset/samples/sample_3.wav"
        

# def main():
#     google_api_key = os.environ.get('GOOGLE_API')
#     speech_to_text = GoogleSpeechToText(google_api_key)

#     audio_file_path = "dataset/samples/sample_2.wav"
#     speech_to_text.transcribe_speech(audio_file_path)


# if __name__ == "__main__":
#     main()
