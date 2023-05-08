import requests


def parse_text(text):
    return text == "true"


def get_response_for(word, get_response=requests.get):
    url = f"http://agilec.cs.uh.edu/spell?check={word}"

    return get_response(url).text


def is_spelling_correct(word):
    return parse_text(get_response_for(word))
