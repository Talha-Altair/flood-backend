from langdetect import detect
from translate import Translator


def detect_language(text):

    try:
        return detect(text)
    except:
        return None


def translate_text(text):

    try:
        translator = Translator(to_lang="en", from_lang=detect_language(text))
        return translator.translate(text)
    except:
        return None


if __name__ == "__main__":

    text = "اهلا اخي الكريم"

    print(detect_language(text))
    print(translate_text(text))
