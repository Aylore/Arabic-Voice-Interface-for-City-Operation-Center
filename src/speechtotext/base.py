from abc import ABC, abstractmethod


class SpeechToText(ABC):
    @abstractmethod
    def transcribe(self):
        pass

    @abstractmethod
    def preprocess(self):
        pass

    @abstractmethod
    def postprocess(self):
        pass
