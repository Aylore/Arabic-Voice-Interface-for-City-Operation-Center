import re
from src.translation.google_translator import GoogleTranslator


def get_questions():
    with open("src/rasa/data/full-example-questions.txt") as f:
        questions = f.read()
        pattern = r"-.*$"
        questions = "\n".join(re.findall(pattern, questions, re.MULTILINE))
        # return questions
        questions = "\n".join(q for q in questions.split("\n") if "intent" not in q)
        # questions = questions.replace("-", "").strip()
        save_to_file(questions, "src/rasa/data/english-questions.txt")
        return questions


def save_to_file(text, path):
    with open(path, "w") as f:
        f.write(text)


def translate_google():
    with open("src/rasa/data/english-questions.txt", "r") as f:
        questions = f.readlines()

    print('translating')
    translated_questions = '\n'.join(GoogleTranslator().translate(q) for q in questions)
    save_to_file(translated_questions, 'src/rasa/data/arabic-questions.txt')
    print('saved')
    # return [GoogleTranslator().translate(q) for q in questions]


# return re.findall('?-', )
# return re.findall("^[\s-]\d+.\s(.*?)$", questions)
# return [
#     re.sub(
#         "\s+",
#         "",
#     )
#     for q in questions
# ]


get_questions()

translate_google()
# print(get_questions())

# import re

# text = """
# - Is the alert id [1234](alert_id) currently open?
# - Can you confirm if the alert id [53431](alert_id) is open?
# - What is the status of the alert id [77343](alert_id)?
# - Provide the current status of the alert id [103434](alert_id).
# - Is the alert id [989838](alert_id) active?
# - Status of the alert id [34343](alert_id)?
# """

# # pattern = r"^[\S-]\d+.\s(.*?)$"
# # questions = re.findall(pattern, text, re.MULTILINE)

# # for question in questions:
# #     print(question)
