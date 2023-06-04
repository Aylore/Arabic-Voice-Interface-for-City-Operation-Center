# speechtotextapp/views.py

from google.cloud import speech_v1p1beta1 as speech
from django.shortcuts import render
from django.conf import settings
from src.google_demo import predict
<<<<<<< HEAD
<<<<<<< HEAD
from src.azure_trans_demo import Translator
from utils.azure_models.azure_speech_to_text import Azure_stt_model
import io, os
=======
from src.azure_demo import predict_live
from src.azure_trans_demo import Translator
=======
from src.azure_demo import predict_live
from src.azure_trans_demo import Translator
from utils.azure_models.azure_speech_to_text import Azure_stt_model
>>>>>>> amgadooz
from .helper import save_audio_file, delete_audio_file
import io, os
import time


<<<<<<< HEAD
>>>>>>> main

trans = Translator()


<<<<<<< HEAD
def save_audio_file(audio_file):
    file_name = "test.wav"
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)

    with open(file_path, "wb") as file_:
        for chunk in audio_file.chunks():
            file_.write(chunk)
    return file_path


def delete_audio_file(file_path):
    try:
        os.remove(file_path)
        print(f"{file_path} has been deleted successfully")
    except OSError as e:
        print(f"Error: {file_path} could not be deleted due to {e}")

=======
>>>>>>> main

=======
trans = Translator()


>>>>>>> amgadooz
def Index(request):
    return render(request, "index.html")


def transcribe(request):
    if request.method == "POST" and request.FILES.get("audio"):
        audio_file = request.FILES["audio"]

<<<<<<< HEAD
        USE_AZURE = True

        if USE_AZURE:
=======
        USE_AZURE = False

        if USE_AZURE:
            # Transcript of the same language
>>>>>>> amgadooz
            audio_path = save_audio_file(audio_file)
            transcript = Azure_stt_model().predict(path=audio_path)
            delete_audio_file(audio_path)
        else:
            audio_data = audio_file.read()
<<<<<<< HEAD
            transcript = predict(audio_data=audio_data)
=======
            # Translated to English
            transcript = Translator().translate_text(predict(audio_data=audio_data)[::-1])

>>>>>>> amgadooz

        return render(request, "index.html", {"transcript": transcript})

    return render(request, "index.html")
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> amgadooz


def transcribe_audio(request):
    if request.method == "POST":
<<<<<<< HEAD
        live_transcript = predict_live()
        return render(request, "index.html", {"live_transcript": live_transcript})
    return render(request, "index.html")

>>>>>>> main
=======
        # Live transcript of the same language
        live_transcript = predict_live()
        return render(request, "index.html", {"live_transcript": live_transcript})
    return render(request, "index.html")
>>>>>>> amgadooz
