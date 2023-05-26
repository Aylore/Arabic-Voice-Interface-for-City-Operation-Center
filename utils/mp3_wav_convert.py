from pydub import AudioSegment
import os
records = os.listdir("benchmark/ar_records_mp3")

print(records)
def mp3_to_wav(src , dst):
    # files
    # convert mp3 to wav
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")

for rec in records:
    mp3_to_wav("benchmark/ar_records_mp3/" + rec , "benchmark/try/" + str(rec[:-4])  + ".wav" )