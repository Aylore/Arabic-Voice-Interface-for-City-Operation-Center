# speechtotextapp/views.py

from google.cloud import speech_v1p1beta1 as speech
from django.shortcuts import render
from django.conf import settings
from src.google_demo import predict
from src.azure_trans_demo import Translator
from utils.azure_models.azure_speech_to_text import Azure_stt_model
from .helper import save_audio_file, delete_audio_file
from django.http import JsonResponse
import io, os
import time


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


import azure.cognitiveservices.speech as speechsdk
from django.http import JsonResponse
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_protect
import time


def transcribe_audio(request):
    start_record = False
    live_transcript = 'oops'
    flag = request.POST.get("new_value")
    if flag is not None:
        start_record = True

    if start_record:
        live_transcript = Azure_stt_model().predict_live()
        return render(request, "index.html", {"live_transcript": live_transcript})

    return render(request, "index.html", {"live_transcript": live_transcript})
