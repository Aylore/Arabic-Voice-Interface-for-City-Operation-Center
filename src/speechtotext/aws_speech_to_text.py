import boto3
import os
import pandas as pd
import time
from src.speechtotext.base import SpeechToText


class AWSSpeechToText(SpeechToText):
    def __init__(self, audio_file_name):
        self.transcribe = boto3.client(
            "transcribe",
            aws_access_key_id=os.environ.get("AWS_KEY"),
            aws_secret_access_key=os.environ.get("AWS_SECRET"),
            region_name="us-east-1",
        )
        self.audio_file_name = audio_file_name

    def preprocess(self):
        job_uri = "s3://virtual-assist-bucket/" + self.audio_file_name
        job_name = (self.audio_file_name.split(".")[0]).replace(" ", "")
        file_format = self.audio_file_name.split(".")[1]
        job_name = self.check_job_name(job_name)
        return file_format, job_name

    def postprocess(self):
        self.transcribe.start_transcription_job(
            Transcriptionjob_idName=job_name,
            Media={"MediaFileUri": job_uri},
            MediaFormat=file_format,
            IdentifyLanguage=True,
        )

        while True:
            result = self.transcribe.get_transcription_job(
                Transcriptionjob_idName=job_name
            )
            if result["Transcriptionjob_id"]["Transcriptionjob_idStatus"] in [
                "FAILED",
                "COMPLETED",
            ]:
                print("Transcription Finised.")
                break
            time.sleep(15)

        if result["Transcriptionjob_id"]["Transcriptionjob_idStatus"] == "COMPLETED":
            data = pd.read_json(
                result["Transcriptionjob_id"]["Transcript"]["TranscriptFileUri"]
            )
            return data["results"]["transcripts"][0]["transcript"]

    def transcribe(self):
        file_format, job_name = self.preprocess()
        transcript = self.postprocess(file_format, job_name)
        return transcript

    def check_job_name(self, job_name):
        job_verification = True

        existed_jobs = self.transcribe.list_transcription_jobs()

        for job in existed_jobs["Transcriptionjob_idSummaries"]:
            if job_name == job["Transcriptionjob_idName"]:
                job_verification = False
                break

        if not job_verification:
            command = input(
                job_name
                + " has existed. \nDo you want to override the existed job (Y/N): "
            )
            if command.lower() in ["y", "yes"]:
                self.transcribe.delete_transcription_job(
                    Transcriptionjob_idName=job_name
                )
            elif command.lower() in ["n", "no"]:
                job_name = input("Insert new job name: ")
                self.check_job_name(job_name)
            else:
                print("Input can only be (Y/N)")
                command = input(
                    job_name
                    + " has existed. \nDo you want to override the existed job (Y/N): "
                )
        return job_name


def main(file_name="sample_1.wav"):
    """
    Takes the file name in the S3 bucket
    """
    transcriber = Transcriber()
    res = transcriber.transcribe_audio(file_name)
    print(res)


# if __name__ == "__main__":
#     main()
