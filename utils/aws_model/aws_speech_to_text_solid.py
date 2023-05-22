import boto3
import os
import pandas as pd
import time

class Transcriber:
    def __init__(self):
        self.transcribe = boto3.client('transcribe',
                                       aws_access_key_id=os.environ.get('AWS_KEY'),
                                       aws_secret_access_key=os.environ.get('AWS_SECRET'),
                                       region_name="us-east-1")

    def check_job_name(self, job_name):
        job_verification = True

        existed_jobs = self.transcribe.list_transcription_jobs()

        for job in existed_jobs['TranscriptionJobSummaries']:
            if job_name == job['TranscriptionJobName']:
                job_verification = False
                break

        if not job_verification:
            command = input(job_name + " has existed. \nDo you want to override the existed job (Y/N): ")
            if command.lower() in ["y", "yes"]:
                self.transcribe.delete_transcription_job(TranscriptionJobName=job_name)
            elif command.lower() in ["n", "no"]:
                job_name = input("Insert new job name: ")
                self.check_job_name(job_name)
            else:
                print("Input can only be (Y/N)")
                command = input(job_name + " has existed. \nDo you want to override the existed job (Y/N): ")
        return job_name

    def transcribe_audio(self, audio_file_name):
        job_uri = "s3://virtual-assist-bucket/" + audio_file_name
        job_name = (audio_file_name.split('.')[0]).replace(" ", "")
        file_format = audio_file_name.split('.')[1]
        job_name = self.check_job_name(job_name)

        self.transcribe.start_transcription_job(
            TranscriptionJobName=job_name,
            Media={'MediaFileUri': job_uri},
            MediaFormat=file_format,
            IdentifyLanguage=True
        )

        while True:
            result = self.transcribe.get_transcription_job(TranscriptionJobName=job_name)
            if result['TranscriptionJob']['TranscriptionJobStatus'] in ['FAILED','COMPLETED']:
                print("Transcription Finised.")
                break
            time.sleep(15)

        if result['TranscriptionJob']['TranscriptionJobStatus'] == "COMPLETED":
            data = pd.read_json(result['TranscriptionJob']['Transcript']['TranscriptFileUri'])
            return data["results"]["transcripts"][0]["transcript"]


def main(file_name ="sample_1.wav"):
    """
        Takes the file name in the S3 bucket
    """
    transcriber = Transcriber()
    res = transcriber.transcribe_audio(file_name)
    print(res)


# if __name__ == "__main__":
#     main()
