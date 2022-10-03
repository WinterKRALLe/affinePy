import string
import unicodedata
from textwrap import wrap

a = 7
b = 3


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


def encode(text):
    #arrX = []
    s = ""
    for i in text:
        if (i == " "):
            s += "XMEZERAX"
            continue
        alphabet = string.ascii_lowercase
        ot = alphabet.find(i)
        X = (a*ot + b) % 26
        # arrX.append(X)
        s += string.ascii_uppercase[X]
    print("encoded:", s)
    return s


def decode(letter):
    s = ""
    letter = str.lower(letter)
    letter = letter.replace("xmezerax", " ")
    for h in letter:
        if h == " ":
            s += " "
            continue
        alphabet = string.ascii_lowercase
        ot = alphabet.find(h)
        #X = (a*ot + b) % 26
        debil = (pow(a, -1, 26)*(ot-b)) % 26
        s += string.ascii_uppercase[debil]
        #s = wrap(s, 5)
    #print("decoded:", " ".join(s))
    print("decoded:", s)


# text = "LOďfl kdsnkjfnk555dgjnkfwaf"
# text = normalizeText(text)
# print("textvoe:", text)
# output = encode(text)
# decoded = decode("RXRV")
