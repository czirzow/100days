# day 31
#force pycharm to read requirements.txt
import pandas as pd
import random



LANGUAGES = {
        'fr': 'French',
        'en': 'English',
        }

class Translator():
    translate_dir = 'lang/'

    def __init__(self, lang_from, lang_to):
        try:

            filename = f"{self.translate_dir}{lang_from}_{lang_to}.csv"
            translate = pd.read_csv(filename)

        except FileNotFoundError as e:
            print(f"Unable to open file: {e}")
            exit()
        else:

            self.lang_from = lang_from.title()
            self.lang_to = lang_to.title()
            self.lookup = {c.lang_from:c.lang_to for (_,c) in translate.iterrows()}

    def get(self):
        word = ""
        translated = ""

        if len(self.lookup):
            word = random.choice(list(self.lookup))
            translated = self.lookup[word]

        return (word, translated)


    def is_correct(self, word, test):
        return self.lookup[word] == test

    def remove(self, word):
        del self.lookup[word]
        pass




if 0 :
    # a sanity check:
    t = Translator('fr', 'en')
    have_a_word = True
    while have_a_word:
        (word, translated) = t.get()
        if word != '':
            print(f"{word}: {translated}")
            t.remove(word)
        else:
            have_a_word = False

