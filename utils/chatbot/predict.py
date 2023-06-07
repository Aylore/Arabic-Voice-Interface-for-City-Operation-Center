import random
from utils.chatbot.train_chatterbot import amg_chatbot

def get_answer(question):
    answer = amg_chatbot.get_response(question)
    return answer

def make_conversation():
    welcome = "bot: Welcome I am your chatbot virtual assistant, How may I help you?"
    goodbye = "Thanks for choosing us, Have a NOICE day!"
    print(welcome)
    while True:
        print(
            random.choices(
                ["Remember if you need to exit type [done] or ctrl+c\n", ""],
                weights=[0.1, 0.9],
            )[0],
            end="",
        )
        try:
            client_question = input("you: ")
            print(f"bot: {get_answer(client_question)}")
            if client_question == "done":
                print(goodbye)
                return
        # Press ctrl-c or ctrl-d on the keyboard to exit
        except (KeyboardInterrupt, EOFError, SystemExit):
            pass


if __name__ == "__main__":
    question = "last online time of the third device"
    answer = get_answer(question)
    print(answer)
    make_conversation()
