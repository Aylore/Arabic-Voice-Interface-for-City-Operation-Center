"""
Module: audio_recorder

    This module provides a class for recording audio from the microphone and saving it to a WAV file.

    Classes:
    - AudioRecorder: Class for recording audio from the microphone and saving it to a WAV file.

    Functions:
    - rec(path): Function to record audio and save it to a file.
    - Parameters:
        - path (str): The path to the file where the recorded audio will be saved.

    Usage:
    - Import the module: import audio_recorder
    - Use the classes and functions:
    - recorder = audio_recorder.AudioRecorder()
    - recorder.record_to_file(path)
    - audio_recorder.rec(path)

    Note:
    - The module requires the 'pyaudio', 'wave', 'array', and 'struct' modules to be installed.
    - The 'AudioRecorder' class provides methods for recording audio and saving it to a WAV file.
    - The 'record' method of the 'AudioRecorder' class records audio from the microphone, normalizes the audio, trims silence from the start and end, and adds padding with 0.5 seconds of blank sound to ensure compatibility with media players.
    - The 'record_to_file' method of the 'AudioRecorder' class records audio and saves it to a specified file path in WAV format.
    - The 'rec' function is a convenience function that calls the 'record_to_file' method of the 'AudioRecorder' class to record audio and save it to a file.
    - The 'rec' function takes a 'path' parameter, which is the path where the recorded audio will be saved.

    
"""


import pyaudio
import wave
from array import array
from struct import pack
from sys import byteorder

class AudioRecorder:
    def __init__(self):
        self.THRESHOLD = 2000       # Threshold for silence detection
        self.CHUNK_SIZE = 1024     # Size of audio chunks to read from the microphone
        self.FORMAT = pyaudio.paInt16   # Audio format
        self.RATE = 44100          # Sample rate

    def is_silent(self, snd_data):
        "Returns 'True' if below the 'silent' threshold"
        return max(snd_data) < self.THRESHOLD

    def normalize(self, snd_data):
        "Average the volume out"
        MAXIMUM = 16384
        times = float(MAXIMUM) / max(abs(i) for i in snd_data)

        r = array('h')
        for i in snd_data:
            r.append(int(i * times))
        return r

    def trim(self, snd_data):
        "Trim the blank spots at the start and end"
        def _trim(snd_data):
            snd_started = False
            r = array('h')

            for i in snd_data:
                if not snd_started and abs(i) > self.THRESHOLD:
                    snd_started = True
                    r.append(i)

                elif snd_started:
                    r.append(i)
            return r

        # Trim to the left
        snd_data = _trim(snd_data)

        # Trim to the right
        snd_data.reverse()
        snd_data = _trim(snd_data)
        snd_data.reverse()
        return snd_data

    def add_silence(self, snd_data, seconds):
        "Add silence to the start and end of 'snd_data' of length 'seconds' (float)"
        silence = [0] * int(seconds * self.RATE)
        r = array('h', silence)
        r.extend(snd_data)
        r.extend(silence)
        return r

    def record(self):
        """
        Record a word or words from the microphone and 
        return the data as an array of signed shorts.

        Normalizes the audio, trims silence from the 
        start and end, and pads with 0.5 seconds of 
        blank sound to make sure VLC et al can play 
        it without getting chopped off.
        """
        p = pyaudio.PyAudio()
        stream = p.open(format=self.FORMAT, channels=1, rate=self.RATE,
                        input=True, output=True,
                        frames_per_buffer=self.CHUNK_SIZE)

        num_silent = 0
        snd_started = False

        r = array('h')

        while 1:
            # Read audio data from the microphone
            snd_data = array('h', stream.read(self.CHUNK_SIZE))
            if byteorder == 'big':
                snd_data.byteswap()
            r.extend(snd_data)

            silent = self.is_silent(snd_data)

            if silent and snd_started:
                num_silent += 1
            elif not silent and not snd_started:
                snd_started = True

            if snd_started and num_silent > 30:
                break

        # Cleanup audio stream and PyAudio instance
        sample_width = p.get_sample_size(self.FORMAT)
        stream.stop_stream()
        stream.close()
        p.terminate()

        # Process audio data
        r = self.normalize(r)
        r = self.trim(r)
        r = self.add_silence(r, 0.5)
        return sample_width, r

    def record_to_file(self, path: str) -> None:
        """Records from the microphone and outputs the resulting data to 'path'"""
        sample_width, data = self.record()
        data = pack('<' + ('h' * len(data)), *data)

        # Write audio data to a WAV file
        wf = wave.open(path, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(sample_width)
        wf.setframerate(self.RATE)
        wf.writeframes(data)

        wf.close()




        

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




if __name__ == "__main__":

    path = "dataset/audio.wav"

    rec(path)