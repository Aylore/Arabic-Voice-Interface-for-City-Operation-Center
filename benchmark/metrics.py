import time
from jiwer import wer
from jiwer import mer
import numpy as np
import torch

class STTEvaluationMetrics:
    def __init__(self):
        self.reference_column = ""
        self.hypothesis_column = ""

    def set_reference_column(self, reference_column):
        self.reference_column = reference_column

    def set_hypothesis_column(self, hypothesis_column):
        self.hypothesis_column = hypothesis_column

    def calculate_wer(self, df):
        reference = df[self.reference_column].tolist()
        hypothesis = df[self.hypothesis_column].tolist()

        total_wer = 0
        num_examples = len(reference)

        for ref, hyp in zip(reference, hypothesis):
            total_wer += wer(ref, hyp)

        return total_wer / num_examples

    def calculate_cer(self, df):
        reference = df[self.reference_column].tolist()
        hypothesis = df[self.hypothesis_column].tolist()

        total_cer = 0
        num_examples = len(reference)

        for ref, hyp in zip(reference, hypothesis):
            total_cer += mer(ref, hyp)

        return total_cer / num_examples

    def calculate_accuracy(self, df):
        reference = df[self.reference_column].tolist()
        hypothesis = df[self.hypothesis_column].tolist()

        total_accuracy = 0
        num_examples = len(reference)

        for ref, hyp in zip(reference, hypothesis):
            ref_words = ref.split()
            hyp_words = hyp.split()
            total_words = len(ref_words)
            correct_words = sum(1 for r, h in zip(ref_words, hyp_words) if r == h)
            total_accuracy += correct_words / total_words

        return total_accuracy / num_examples

    def calculate_perplexity(self, df, language_model):
        hypothesis = df[self.hypothesis_column].tolist()
        total_perplexity = 0
        num_examples = len(hypothesis)

        for hyp in hypothesis:
            tokens = hyp.split()
            input_tensor = torch.tensor([language_model.vocab[token] for token in tokens])
            output = language_model(input_tensor.unsqueeze(0))
            perplexity = torch.exp(output)
            total_perplexity += perplexity.item()

        return total_perplexity / num_examples

    def measure_latency(self, df, speech_input, stt_model):
        start_time = time.time()
        for _ in range(len(df)):
            _ = stt_model.transcribe(speech_input)
        end_time = time.time()

        latency = (end_time - start_time) / len(df)
        return latency

    def measure_processing_speed(self, df, speech_input, num_iterations, stt_model):
        start_time = time.time()
        for _ in range(len(df) * num_iterations):
            _ = stt_model.transcribe(speech_input)
        end_time = time.time()

        processing_time = end_time - start_time
        processing_speed = (len(df) * num_iterations) / processing_time
        return processing_speed
