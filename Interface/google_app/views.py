# speechtotextapp/views.py

from django.shortcuts import render
from django.conf import settings
from final_pipeline import main
from .helper import save_audio_file, delete_audio_file
import io, os
import time


# trans = Translator()


def Index(request):
    return render(request, "index.html")


def transcribe(request):
    # pass 
    if request.method == "POST" and request.FILES.get("audio"):
        audio_file = request.FILES["audio"]
        audio_path = save_audio_file(audio_file)
        transcript = main(audio_path)
        delete_audio_file(audio_path)


    #     USE_AZURE = False

    #     if USE_AZURE:
    #         # Transcript of the same language
    #         audio_path = save_audio_file(audio_file)
    #         transcript = Azure_stt_model().predict(path=audio_path)
    #         delete_audio_file(audio_path)
    #     else:
    #         audio_data = audio_file.read()
    #         # Translated to English
    #         transcript = Translator().translate_text(predict(audio_data=audio_data)[::-1])


        return render(request, "index.html", {"transcript": transcript})

    return render(request, "index.html")


def transcribe_audio(request):
    if request.method == "POST":
        live_transcript = main()
        return render(request, "index.html", {"live_transcript": live_transcript})
    return render(request, "index.html")



# import subprocess

# def your_view(request):

