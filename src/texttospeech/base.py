from abc import ABC, abstractmethod

class TextToSpeech(ABC):
    @abstractmethod
    def read_aloud(self, text, target):
        pass

    @abstractmethod
    def preprocess(self, text):
        pass

    @abstractmethod
    def postprocess(self, response):
        pass

