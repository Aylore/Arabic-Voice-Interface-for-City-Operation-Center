from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_first_response
from chatterbot.comparisons import LevenshteinDistance

database_path = "utils/chatbot/db/database.db"

amg_chatbot = ChatBot(
    "amgadooz",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri=f"sqlite:///{database_path}",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": LevenshteinDistance,
            "response_selection_method": get_first_response,
        },
    ],
    read_only=True,  # disable learning while talking live
)


def train(chatbot, custom_corpus_path="utils/chatbot/chatbot_dataset.json"):
    trainer = ChatterBotCorpusTrainer(amg_chatbot)
    trainer.train(
        custom_corpus_path,
        "chatterbot.corpus.english.greetings",
        "chatterbot.corpus.english.conversations",
    )


if __name__ == "__main__":
    train(amg_chatbot)
