"""

    This module provides functions for converting MP3 files to WAV format using the 'pydub' library.

    Functions:
    - mp3_to_wav(src, dst): Function to convert an MP3 file to WAV format.
    - Parameters:
        - src (str): The path of the source MP3 file.
        - dst (str): The path where the converted WAV file will be saved.

    Usage:
    - Import the module: import mp3_converter
    - Use the functions:
    - mp3_converter.mp3_to_wav(src, dst)

    Note:
    - The module requires the 'pydub' and 'os' modules to be installed.
    - The 'mp3_to_wav' function converts an MP3 file to WAV format using the 'AudioSegment' class from the 'pydub' library.
    - The 'mp3_to_wav' function takes a 'src' parameter, which is the path of the source MP3 file, and a 'dst' parameter, which is the path where the converted WAV file will be saved.
    - The 'mp3_to_wav' function uses the 'from_mp3' method of the 'AudioSegment' class to load the MP3 file, and the 'export' method to save it as a WAV file.
    - The 'mp3_to_wav' function assumes that the 'pydub' library is properly installed and configured.


"""



from pydub import AudioSegment
import os
records = os.listdir("benchmark/ar_records_mp3")

print(records)
def mp3_to_wav(src , dst):
    """
        - mp3_to_wav(src, dst): Function to convert an MP3 file to WAV format.
        - Parameters:
            - src (str): The path of the source MP3 file.
            - dst (str): The path where the converted WAV file will be saved.
    """
    # files
    # convert mp3 to wav
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")

for rec in records:
    mp3_to_wav("benchmark/ar_records_mp3/" + rec , "benchmark/try/" + str(rec[:-4])  + ".wav" )