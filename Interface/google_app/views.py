"""
This module contains functions for transcribing audio files and streaming audio from the default input device.

The module provides three functions: Index, transcribe, and transcribe_audio. 
1- Index renders the index.html template, which allows users to upload an audio file for transcription. 
2- transcribe transcribes an uploaded audio file and displays the transcript on the index.html template. 
3- transcribe_audio transcribes audio from the default input device and displays the live transcript on the index.html template.

Helper functions for saving and deleting audio files are also included in the helper module.
"""

from django.shortcuts import render
from django.conf import settings
from final_pipeline import main
from .helper import save_audio_file, delete_audio_file
import io, os
import time


def Index(request):
    """
    Renders the index.html template.

    This function renders the index.html template, which displays a form to upload an audio file and transcribe it.

    Args:
        request: The HTTP request object.

    Returns:
        The HTTP response object containing the rendered index.html template.
    """
    return render(request, "index.html")


def transcribe(request):
    """
    Transcribes an uploaded audio file.

    This function transcribes an uploaded audio file and displays the resulting transcript on the index.html template.

    Args:
        request: The HTTP request object. Must contain a "POST" request with an "audio" file.

    Returns:
        The HTTP response object containing the rendered index.html template with the transcript.
    """
    if request.method == "POST" and request.FILES.get("audio"):
        audio_file = request.FILES["audio"]
        audio_path = save_audio_file(audio_file)
        transcript, enhance = main(audio_path)
        delete_audio_file(audio_path)
        return render(request, "index.html", {"transcript": transcript, 'enhance': enhance})
    return render(request, "index.html")


def transcribe_audio(request):
    """
    Transcribes audio from the default audio input device.

    This function transcribes audio from the default audio input device and displays the resulting live transcript on the index.html template.

    Args:
        request: The HTTP request object. Must contain a "POST" request.

    Returns:
        The HTTP response object containing the rendered index.html template with the live transcript.
    """
    if request.method == "POST":
        live_transcript, enhance = main()
        return render(request, "index.html", {"live_transcript": live_transcript, 'enhance': enhance})
    return render(request, "index.html")