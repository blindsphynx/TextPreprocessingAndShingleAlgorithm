from ReadDictClass import getDictList
from Lemmatization import lemmatization
import os
import re

conjunctionPath = "..\\Dictionaries\\conjunctions.txt"
prepositionPath = "..\\Dictionaries\\prepositions.txt"
particlePath = "..\\Dictionaries\\particles.txt"
interjectionPath = "..\\Dictionaries\\interjections.txt"
pronounsPath = "..\\Dictionaries\\pronouns.txt"
punctuationPath = "..\\Dictionaries\\punctuationMarks.txt"


class TextProcessing:
    def __init__(self, text):
        if text == "" or type(text) is not str:
            raise Exception("Empty text or not string")

        EngToRuDict = {65: 1040, 66: 1042, 67: 1057, 69: 1045, 79: 1054, 80: 1056, 72: 1053, 84: 1058, 97: 1072,
                       99: 1089, 101: 1077, 111: 1086, 112: 1088, 120: 1093, 121: 1091}

        for i in range(len(text)):
            if str.isalpha(text[i]):
                if not 1040 <= ord(text[i]) <= 1103:
                    try:
                        text = text[:i] + chr(EngToRuDict[ord(text[i])]) + text[i + 1:]
                    except KeyError:
                        print("Undefined symbol {} in text".format(text[i]))
                        continue

        self._text = text

    def deleteDigits(self):
        self._text = re.sub(r"\d-[а-я]*", ' ', self._text)   # delete nums with endings which start with a dash ("1-ый")
        self._text = re.sub(r"\d[а-я]*", ' ', self._text)    # delete nums with endings without a dash ("1ый")
        self._text = re.sub(r"\d", ' ', self._text)          # delete the rest of nums

    def collectAllStopWords(self):
        allStopWords = set(getDictList(conjunctionPath, prepositionPath,
                                       interjectionPath, particlePath, pronounsPath))
        punctuationMarks = set(getDictList(punctuationPath))
        # delete digits here, otherwise ordinal digits won't be deleted
        self.deleteDigits()

        for sign in punctuationMarks:
            self._text = self._text.replace(sign, ' ')
        return allStopWords

    def processText(self):
        setOfStopWords = self.collectAllStopWords()

        self._text = self._text.replace('\r', ' ')
        tempText = self._text.split(' ')

        for i in range(0, len(tempText)):
            if tempText[i].lower().replace('\r', '').replace('\n', '') in setOfStopWords:
                tempText[i] = ''
            else:
                tempText[i] = tempText[i].lower().replace('\n', '')

        resultText = []
        it = 0
        while it < len(tempText):
            if tempText[it] != '':
                resultText.append(tempText[it])
                del tempText[it]
            else:
                it += 1
        resultText = lemmatization(resultText)
        return resultText
