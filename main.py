import json
from pprint import pprint
from UI import Ui


def translate(word):
    code = get_morse_code()


def get_morse_code() -> dict:
    """Returns a dictionary with keys the characters and values their morse translation"""
    with open("./morsecode.json", 'r') as file:
        d = json.load(file)
    return d

if __name__ == '__main__':
    window = Ui(translate_func=translate)


    





if __name__ == '__main__':
    loop()