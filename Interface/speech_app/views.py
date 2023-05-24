# speechtotextapp/views.py

from google.cloud import speech_v1p1beta1 as speech
from django.shortcuts import render

def Index(request):
    return render(request, 'index.html')

def transcribe(request):
    if request.method == 'POST' and request.FILES.get('audio'):
        audio_file = request.FILES['audio']

        # Configure speech recognition settings
        client = speech.SpeechClient()
        language_code = 'en-US'  # English
        if request.POST.get('language') == 'ar':
            language_code = 'ar'  # Arabic

        # Read the audio file content
        audio_content = audio_file.read()

        # Configure the audio settings
        audio = speech.RecognitionAudio(content=audio_content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code=language_code,
        )

        # Perform the speech-to-text transcription
        response = client.recognize(config=config, audio=audio)

        # Extract the transcriptions from the response
        transcriptions = [result.alternatives[0].transcript for result in response.results]

        # Return the transcriptions to the template
        return render(request, 'index.html', {'transcriptions': transcriptions})

    return render(request, 'index.html')
