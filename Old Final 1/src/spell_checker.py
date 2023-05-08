import requests as requests


def parse_text(text):
    return text == "true"


def get_response_for(word, get_request=requests.get):
    url = f"http://agilec.cs.uh.edu/spell?check={word}"

    return get_request(url).text


def is_spelling_correct(word):
    return parse_text(get_response_for(word))
