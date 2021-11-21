from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""
    A = set(a.split('\n'))
    B = set(b.split('\n'))

    return A.intersection(B)


def sentences(a, b):
    """Return sentences in both a and b"""

    A = set(sent_tokenize(a))
    B = set(sent_tokenize(b))

    return A & B


def subtoken(str, N):
    substr = []

    for i in range(len(str) - N + 1):
        substr.append(str[i: i + N])

    return substr


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    A = set(subtoken(a, n))
    B = set(subtoken(b, n))

    return A & B
