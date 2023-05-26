import os
from django.conf import settings


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