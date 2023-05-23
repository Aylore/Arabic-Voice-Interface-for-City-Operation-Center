from utils.azure_models.azure_speech_to_text import Azure_stt_model
import os
import pandas as pd

recs = os.listdir("dataset/en_records_wav")
df = pd.read_csv("benchmark/azure_benchmark/csv files/en_data.csv")["text"]

stt = Azure_stt_model()

res = []
i = 0
for rec in recs:
    i = i + 1
    try:
        cur_res = stt.predict(path="dataset/en_records_wav" + rec )
        res.append([rec , df[int(rec[:-4])] ,cur_res ])
        print(f"record{i}")
    except:
        break

df2 = pd.DataFrame(res, columns = ['file', 'true label', 'pred'])

#df2.to_csv("benchmark/azure_benchmark/csv files/azure_en_results.csv")