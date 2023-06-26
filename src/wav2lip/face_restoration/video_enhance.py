import cv2
import os
import shutil
import subprocess


def codeformer_init():
    model_path = "/Users/aleedo/Coding/ITI/9-Months/Final-Project/Arabic-Voice-Interface-for-City-Operation-Center/src/wav2lip/face_restoration/CodeFormer"

    if not os.path.exists(model_path):
        print("CodeFormer Setup Started ...")

        command = "git clone https://github.com/sczhou/CodeFormer.git"
        command_req = "cd /Users/aleedo/Coding/ITI/9-Months/Final-Project/Arabic-Voice-Interface-for-City-Operation-Center/src/wav2lip/face_restoration/CodeFormer && pip install -r requirements.txt"

        subprocess.call(command, shell=True)
        subprocess.call(command_req, shell=True)

        # install basicsr

        command_basicsr = "cd /Users/aleedo/Coding/ITI/9-Months/Final-Project/Arabic-Voice-Interface-for-City-Operation-Center/src/wav2lip/face_restoration/CodeFormer && python basicsr/setup.py develop"
        subprocess.call(command_basicsr, shell=True)

        # get pretrained models
        command_facelib = "cd /Users/aleedo/Coding/ITI/9-Months/Final-Project/Arabic-Voice-Interface-for-City-Operation-Center/src/wav2lip/face_restoration/CodeFormer && python scripts/download_pretrained_models.py facelib"
        command_codeformer = "cd /Users/aleedo/Coding/ITI/9-Months/Final-Project/Arabic-Voice-Interface-for-City-Operation-Center/src/wav2lip/face_restoration/CodeFormer && python scripts/download_pretrained_models.py CodeFormer"

        subprocess.call(command_facelib, shell=True)
        subprocess.call(command_codeformer, shell=True)

        print("CodeFormer Setup Completed!")


def enhance(video_path, output_path):
    command = f"cd /Users/aleedo/Coding/ITI/9-Months/Final-Project/Arabic-Voice-Interface-for-City-Operation-Center/src/wav2lip/face_restoration && python CodeFormer/inference_codeformer.py -w 0.95 --input_path {video_path} --bg_upsampler weights/realesrgan -o {output_path}"
    subprocess.call(command, shell=True)


def main(
    video_path="/Users/aleedo/Coding/ITI/9-Months/Final-Project/Arabic-Voice-Interface-for-City-Operation-Center/Interface/google_app/static/result_voice.mp4",
    output_path="/Users/aleedo/Coding/ITI/9-Months/Final-Project/Arabic-Voice-Interface-for-City-Operation-Center/Interface/google_app/static/enhancement",
):
    codeformer_init()

    if os.path.exists(output_path):
        shutil.rmtree(output_path)

    enhance(video_path, output_path)


if __name__ == "__main__":
    main(
        video_path="/Users/aleedo/Coding/ITI/9-Months/Final-Project/Arabic-Voice-Interface-for-City-Operation-Center/Interface/google_app/static/result_voice.mp4"
        # video_path="src/wav2lip/videos/test-old.mp4"
        # output_path='src/wav2lip/face_restoration'
    )
