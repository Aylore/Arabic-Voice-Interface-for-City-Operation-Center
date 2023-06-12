# speechtotextapp/views.py

from google.cloud import speech_v1p1beta1 as speech
from django.shortcuts import render
from django.conf import settings
from src.google_demo import predict
from src.azure_demo import predict_live
from src.azure_trans_demo import Translator
from src.final_pipeline import come_on
from utils.azure_models.azure_speech_to_text import Azure_stt_model
from .helper import save_audio_file, delete_audio_file
import io, os
import time


trans = Translator()


def Index(request):
    return render(request, "index.html")


def transcribe(request):
    if request.method == "POST" and request.FILES.get("audio"):
        audio_file = request.FILES["audio"]

        USE_AZURE = False

        if USE_AZURE:
            # Transcript of the same language
            audio_path = save_audio_file(audio_file)
            transcript = Azure_stt_model().predict(path=audio_path)
            delete_audio_file(audio_path)
        else:
            audio_data = audio_file.read()
            # Translated to English
            transcript = Translator().translate_text(predict(audio_data=audio_data)[::-1])


        return render(request, "index.html", {"transcript": transcript})

    return render(request, "index.html")


def transcribe_audio(request):
    if request.method == "POST":
        # Live transcript of the same language
        # live_transcript = predict_live()
        live_transcript = come_on()
        return render(request, "index.html", {"live_transcript": live_transcript})
    return render(request, "index.html")
