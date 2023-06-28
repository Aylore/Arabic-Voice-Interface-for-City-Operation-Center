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
<<<<<<< HEAD
        transcript, enhance = main(audio_path)
        delete_audio_file(audio_path)
        return render(request, "index.html", {"transcript": transcript, 'enhance': enhance})
=======
<<<<<<< HEAD
        transcript, enhance = main(audio_path)
        delete_audio_file(audio_path)
        return render(request, "index.html", {"transcript": transcript, 'enhance': enhance})
=======
        transcript = main(audio_path)
        delete_audio_file(audio_path)
        return render(request, "index.html", {"transcript": transcript})
>>>>>>> main
>>>>>>> main
    return render(request, "index.html")


    # return render(request, "index.html")

def transcribe_audio(request):
    if request.method == "POST":
<<<<<<< HEAD
        live_transcript, enhance = main()
        return render(request, "index.html", {"live_transcript": live_transcript, 'enhance': enhance})
=======
<<<<<<< HEAD
        live_transcript, enhance = main()
        return render(request, "index.html", {"live_transcript": live_transcript, 'enhance': enhance})
=======
        live_transcript = main()
        return render(request, "index.html", {"live_transcript": live_transcript})
>>>>>>> main
>>>>>>> main
    return render(request, "index.html")