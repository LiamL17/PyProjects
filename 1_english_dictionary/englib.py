from difflib import get_close_matches

import json

def main():
    data = json.load(open('../data/data.json', 'r'))
    out = get_input(data)
    print('')
    if type(out) == list:
        for i in out:
            print(i)
    else:
        print(out)
    print('')


def get_input(data):
    word = input('Please type your word -> ').lower()
    if word in data:
        return data[word]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        word_close = get_close_matches(word, data.keys(), cutoff=0.7)
        if word_close != []:
            word_close = word_close[0]
            yorn = input("Found '{}' instead of '{}', would you like to continue, Y (yes) or N (no), -> ".format(word_close, word)).lower()
            if yorn == 'y':
                return data[word_close]
            elif yorn == 'n':
                return 'Word does not exist, please double check it.'
            else:
                return "I didn't quite understand that :("
        else: return 'Could not find that word.'

if __name__ == "__main__":
    main()