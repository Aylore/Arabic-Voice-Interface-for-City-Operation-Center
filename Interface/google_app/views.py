# speechtotextapp/views.py

from google.cloud import speech_v1p1beta1 as speech
from django.shortcuts import render
from django.conf import settings
from src.google_demo import predict
from src.azure_demo import predict_live
from src.azure_trans_demo import Translator
from .helper import save_audio_file, delete_audio_file
import io, os
import time

#israa is here 

trans = Translator()



def Index(request):
    return render(request, "index.html")


def transcribe(request):
    if request.method == "POST" and request.FILES.get("audio"):
        audio_file = request.FILES["audio"]

        USE_AZURE = True

        if USE_AZURE:
            audio_path = save_audio_file(audio_file)
            transcript = Azure_stt_model().predict(path=audio_path)
            delete_audio_file(audio_path)
        else:
            audio_data = audio_file.read()
            transcript = predict(audio_data=audio_data)

        return render(request, "index.html", {"transcript": transcript})

    return render(request, "index.html")


def transcribe_audio(request):
    if request.method == "POST":
        live_transcript = predict_live()
        return render(request, "index.html", {"live_transcript": live_transcript})
    return render(request, "index.html")

