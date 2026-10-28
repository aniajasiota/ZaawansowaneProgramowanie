import string

def word_frequencies(text: str) -> dict:
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    result = {}

    for word in text.split():
        if word not in result:
            result[word] = 1
        else:
            result[word] += 1

    return result