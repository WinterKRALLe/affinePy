import string
import unicodedata
from textwrap import wrap


def encoding(text):
    text = unicodedata.normalize('NFD', text)
    text = u"".join([c for c in text if not unicodedata.combining(c)])
    return text


def lowerAndPunctuation(text):
    text.translate(str.maketrans('', '', string.punctuation))
    text = str.lower(text)
    return text


def normalizeText(text):
    text = lowerAndPunctuation(text)
    text = encoding(text)
    return text
