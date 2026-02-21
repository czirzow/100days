import pandas as pd
import random

LANGUAGES = {
        'fr': 'French',
        'en': 'English',
        }

class Translated():

    def __init__(self, lang, word, translated):
        self.lang = lang
        self.native = word 
        self.value = translated


class Translator():
    """read a file from {lang_dir}/{lang_from}_{lang_to}.csv"""


    def __init__(self, lang_from: str, lang_to:str, dir:str = "lang/") -> None:
        """ something like:
        t = Translator('de', 'fr', dir='.langs/')
        """
        try:
            self.translation_dir = dir
            self.lang = {'from': LANGUAGES[lang_from],
                         'to': LANGUAGES[lang_to]}
            filename = f"{dir}{lang_from}_{lang_to}.csv"

            translate = pd.read_csv(filename)


        except FileNotFoundError as e:
            print(f"Unable to open file: {e}")
            exit()
        except pd.errors.EmptyDataError as e:
            print(f"Problem parsing file: {e}")
            pass
        except pd.errors.ParserError as e:
            print(f"Problem parsing file: {e}")
            pass
        else:

            self.lang_from = lang_from.title()
            self.lang_to = lang_to.title()
            self.lookup = {c.lang_from:c.lang_to for (_,c) in translate.iterrows()}

    def get_translated(self):
        if len(self.lookup):
            word = random.choice(list(self.lookup))
            translated = self.lookup[word]
            return Translated(self.lang, word, translated)

    def get(self):
        """returns a tuple with (lang_from, lang_to)"""
        
        lang_from = ""
        lang_to = ""

        if len(self.lookup):
            lang_from = random.choice(list(self.lookup))
            lang_to = self.lookup[lang_from]

        return (lang_from, lang_to)

    def remove(self, word):
        """remove a word from the list so it won't be returned again"""
        del self.lookup[word]

