from abc import ABC, abstractmethod

class Translator(ABC):
    @abstractmethod
    def translate(self, text, target):
        pass

    @abstractmethod
    def preprocess(self, text):
        pass

    @abstractmethod
    def postprocess(self, response):
        pass

