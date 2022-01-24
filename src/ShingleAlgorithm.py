import hashlib


def divideTextIntoShingles(list_):
    text = list_
    shingleSize = 5
    hashedText = []
    shingles = [text[i:i + shingleSize] for i in range(len(text))][:-shingleSize]
    for shingle in shingles:
        hash_obj = hashlib.sha1(' '.join(shingle).encode()).hexdigest()
        hashedText.append(hash_obj)
    return hashedText
