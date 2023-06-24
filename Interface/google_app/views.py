from django.shortcuts import render
from django.conf import settings
from final_pipeline import main
from .helper import save_audio_file, delete_audio_file
import io, os
import time


def Index(request):
    return render(request, "index.html")


def transcribe(request):
    if request.method == "POST" and request.FILES.get("audio"):
        audio_file = request.FILES["audio"]
        audio_path = save_audio_file(audio_file)
        transcript, enhance = main(audio_path)
        delete_audio_file(audio_path)
        return render(request, "index.html", {"transcript": transcript, 'enhance': enhance})
    return render(request, "index.html")


def transcribe_audio(request):
    if request.method == "POST":
        live_transcript, enhance = main()
        return render(request, "index.html", {"live_transcript": live_transcript, 'enhance': enhance})
    return render(request, "index.html")