import pymorphy2

morph = pymorphy2.MorphAnalyzer()


def lemmatization(text):
    text = ' '.join(text)
    words = text.split()
    res = []
    for word in words:
        temp = morph.parse(word)[0]
        res.append(temp.normal_form)
    return res
