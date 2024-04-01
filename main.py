import json
from pprint import pprint

def get_morse_code() -> dict:
    """Returns a dictionary with keys the characters and values their morse translation"""
    with open("./morsecode.json", 'r') as file:
        d = json.load(file)
    return d

def ask_for_word() -> str:
    """Function that handles the word input"""
    word = input('Enter the word you want to translate:').casefold()
    code = get_morse_code()
    for letter in word:
        if letter not in code.keys():
            print(f'Unrecognised character {letter} please try another word.')
            return ask_for_word()
    return word

def continue_running() -> None:
    """Function that handles if user wants to continue translating"""
    choice = input("Do you want to transate another word?[Y-N]")
    if choice.capitalize() == 'N':
        print('Okey bye.')
        return
    elif choice.capitalize() == 'Y':
        loop()
    else:
        print(f'Unrecognised choice {choice} please select again')
        continue_running()

def loop():
    """Main Program Loop"""
    word = ask_for_word()
    code = get_morse_code()
    translated = ""

    # translate
    for letter in word:
        translated += code[letter]
        translated += ' '
    
    print(f'Your translated word is: {translated}')
    continue_running()
    return
    





if __name__ == '__main__':
    loop()