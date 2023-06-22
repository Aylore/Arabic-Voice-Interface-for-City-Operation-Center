import cv2
import os

import subprocess



def codeformer_init():
    
    model_path = "Waw2Lip/CodeFormer/"
    if not os.path.exists(model_path):
        print("CodeFormer Setup Started ...")

        command = "cd src/face_restoration && git clone https://github.com/sczhou/CodeFormer.git"
        command_req = "cd src/face_restoration/CodeFormer && pip install -r requirements.txt"

        subprocess.call(command , shell=True)
        subprocess.call(command_req , shell=True)

        #install basicsr
        
        command_basicsr = 'cd src/face_restoration/CodeFormer && python basicsr/setup.py develop'
        subprocess.call(command_basicsr , shell=True)

        # get pretrained models
        command_facelib = "cd src/face_restoration/CodeFormer && python scripts/download_pretrained_models.py facelib"
        command_codeformer = "cd src/face_restoration/CodeFormer && python scripts/download_pretrained_models.py CodeFormer"

        subprocess.call(command_facelib , shell=True)
        subprocess.call(command_codeformer , shell=True)

        print("CodeFormer Setup Completed!")



def enhance(video_path , output_path):
    command = f"python inference_codeformer.py -w 0.95 --input_path {video_path} --bg_upsampler realesrgan -o {output_path}"
    subprocess.call(command , shell=True)

def main(video_path , output_path="results/enhnaced/"):
    codeformer_init()


    
    # if not os.path.exists(output_path):
    #     os.mkdir(output_path)

    # enhance(video_path , output_path)

    



    






if __name__ == "__main__":
    main(video_path="Wav2Lip/00006.mp4" )


