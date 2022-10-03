import string
import unicodedata


def encoding(text):
    text = unicodedata.normalize('NFD', text)
    text = u"".join([c for c in text if not unicodedata.combining(c)])
    return text


def lowerAndPunctuation(text):
    punc = '''!()-[]{};:'"\,<>./?@#ˇ$%^&*_~'''
    for ele in text:
        if ele in punc:
            text = text.replace(ele, "")
    text = str.lower(text)
    return text


def normalizeText(text):
    text = lowerAndPunctuation(text)
    text = encoding(text)
    return text
