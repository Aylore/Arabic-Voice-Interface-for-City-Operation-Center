# speechtotextapp/views.py

from google.cloud import speech_v1p1beta1 as speech
from django.shortcuts import render
from src.google_demo import predict
from src.azure_trans_demo import Translator

trans = Translator()


def Index(request):
    return render(request, "index.html")


def transcribe(request):
    if request.method == "POST" and request.FILES.get("audio"):
        audio_file = request.FILES["audio"]

        # Read the audio file content
        audio_data = audio_file.read()
        print(audio_data)

        # English Transcript, Translating Arabic to English, or keeping it English
        transcript = trans.translate_text(predict(audio_data=audio_data))

        # Return the transcriptions to the template
        return render(request, "index.html", {"transcript": transcript})

    return render(request, "index.html")
