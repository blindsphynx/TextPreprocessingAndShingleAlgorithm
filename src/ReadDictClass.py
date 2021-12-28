import codecs


def getDictList(*paths) -> list:
    listOfStopWords = []
    for path in paths:
        file = codecs.open(path, encoding='utf-8')
        listOfStopWords += file.read().replace('\r', '').split('\n')
        file.close()
    return listOfStopWords
