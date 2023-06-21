import cv2
import os

import subprocess


def codeformer_init():
    model_path = "/Users/aleedo/Coding/ITI/9-Months/Final-Project/Arabic-Voice-Interface-for-City-Operation-Center/src/wav2lip/face_restoration/CodeFormer"
    if not os.path.exists(model_path):
        print("CodeFormer Setup Started ...")

        command = "git clone https://github.com/sczhou/CodeFormer.git"
        command_req = "cd CodeFormer && pip install -r requirements.txt"

        subprocess.call(command, shell=True)
        subprocess.call(command_req, shell=True)

        # install basicsr

        command_basicsr = "cd CodeFormer && python basicsr/setup.py develop"
        subprocess.call(command_basicsr, shell=True)

        # get pretrained models
        command_facelib = (
            "cd CodeFormer && python scripts/download_pretrained_models.py facelib"
        )
        command_codeformer = (
            "cd CodeFormer && python scripts/download_pretrained_models.py CodeFormer"
        )

        subprocess.call(command_facelib, shell=True)
        subprocess.call(command_codeformer, shell=True)

        print("CodeFormer Setup Completed!")


def enhance(video_path, output_path):
    command = f"python /Users/aleedo/Coding/ITI/9-Months/Final-Project/Arabic-Voice-Interface-for-City-Operation-Center/src/wav2lip/face_restoration/CodeFormer/inference_codeformer.py -w 0.95 --input_path {video_path} --bg_upsampler realesrgan -o {output_path}"
    subprocess.call(command, shell=True)


def main(
    video_path="/Users/aleedo/Coding/ITI/9-Months/Final-Project/Arabic-Voice-Interface-for-City-Operation-Center/Interface/google_app/static/result_voice.mp4",
    output_path="/Users/aleedo/Coding/ITI/9-Months/Final-Project/Arabic-Voice-Interface-for-City-Operation-Center/Interface/google_app/static/",
):
    # codeformer_init()

    if not os.path.exists(output_path):
        os.mkdir(output_path)
    enhance(video_path, output_path)


if __name__ == "__main__":
    main(
        video_path="/Users/aleedo/Coding/ITI/9-Months/Final-Project/Arabic-Voice-Interface-for-City-Operation-Center/Interface/google_app/static/result_voice.mp4"
    )
