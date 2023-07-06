"""
    This module provides functions for initializing and using the CodeFormer model for face restoration.

    Functions:
    - codeformer_init(): Initialize the CodeFormer model by setting up the required dependencies and downloading pretrained models.
    - enhance(video_path, output_path): Enhance a video by applying the CodeFormer model to perform face restoration.
    - main(video_path, output_path): The main function to run the face restoration process using the CodeFormer model.

    Note: This module relies on external dependencies such as Git, pip, and specific scripts from the CodeFormer repository.
    Make sure these dependencies are properly installed before using this module.
    
"""





import os
import cv2
import shutil
import subprocess
from const import ENHANCE_MODEL, GENERATED_VIDEO, ENHANCED_GENERATED_VIDEO


def codeformer_init():
    model_path = ENHANCE_MODEL

    if not os.path.exists(model_path):
        print("CodeFormer Setup Started ...")

        command = "git clone https://github.com/sczhou/CodeFormer.git"
        command_req = f"cd {ENHANCE_MODEL} && pip install -r requirements.txt"

        subprocess.call(command, shell=True)
        subprocess.call(command_req, shell=True)

        # install basicsr

        command_basicsr = "cd {ENHANCE_MODEL} && python basicsr/setup.py develop"
        subprocess.call(command_basicsr, shell=True)

        # get pretrained models
        command_facelib = "cd {ENHANCE_MODEL} && python scripts/download_pretrained_models.py facelib"
        command_codeformer = "cd {ENHANCE_MODEL} && python scripts/download_pretrained_models.py CodeFormer"

        subprocess.call(command_facelib, shell=True)
        subprocess.call(command_codeformer, shell=True)

        print("CodeFormer Setup Completed!")


def enhance(video_path, output_path):
    """
         Enhance a video by applying the CodeFormer model to perform face restoration.
    """

    command = f"cd {ENHANCE_MODEL} && python inference_codeformer.py -w 0.95 --input_path {video_path} --bg_upsampler weights/realesrgan -o {output_path}"
    subprocess.call(command, shell=True)


def main(
    video_path=GENERATED_VIDEO,
    output_path=ENHANCED_GENERATED_VIDEO,
):
    codeformer_init()

    if os.path.exists(output_path):
        shutil.rmtree(output_path)

    enhance(video_path, output_path)


if __name__ == "__main__":
    main(
        video_path="Interface/google_app/static/result_voice.mp4"
        # video_path="src/wav2lip/videos/test-old.mp4"
        # output_path='src/wav2lip/face_restoration'
    )
