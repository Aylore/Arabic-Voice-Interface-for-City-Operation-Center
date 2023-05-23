import pandas as pd
import os 

from src import google_demo

from pydub import AudioSegment
from benchmark.metrics import STTEvaluationMetrics



# parent_path = "benchmark/records-20230522T205605Z-001/records/"


# df = pd.read_csv("benchmark/data.csv")

# df = df[["sentence"]]

# recs = os.listdir("benchmark/records-20230522T205605Z-001/records/")


def mp3_to_wav(src , dst):
    # files
    

    # convert mp3 to wav
    sound = AudioSegment.from_mp3(src)
    sound.export( dst, format="wav")



# for rec in recs:
#     mp3_to_wav(parent_path + rec , "benchmark/wav_recs/" + str(rec[:-4])  + ".wav" )


wav_recs = os.listdir("benchmark/wav_recs/")


# res = []

# for wav_rec in wav_recs:
#     cur_res = google_demo.predict(path="benchmark/wav_recs/" + wav_rec )
#     res.append(( wav_rec , cur_res ))
    



df_eval = pd.read_csv("benchmark/google_bench.csv" , index_col=0)




# Instantiate the STTEvaluationMetrics object
eval_metrics = STTEvaluationMetrics()

# Set the reference and hypothesis columns
eval_metrics.set_reference_column('sentence')
eval_metrics.set_hypothesis_column('pred')

# Calculate the evaluation metrics
wer = eval_metrics.calculate_wer(df_eval)
cer = eval_metrics.calculate_cer(df_eval)
accuracy = eval_metrics.calculate_accuracy(df_eval)

print(f"Word Error Rate (WER): {wer}")
print(f"Character Error Rate (CER): {cer}")
print(f"Accuracy: {accuracy}")