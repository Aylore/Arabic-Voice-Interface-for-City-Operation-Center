from utils.record_audio import AudioRecorder



def rec(path):
    """
        Takes path for saving the file
    """


    record = AudioRecorder()
    try :
        record.record_to_file(path)
        print("Record Finised")
    except Exception as ex:
        print(f"Record Failed : {ex}")




rec("benchmark/test_rec.wav")