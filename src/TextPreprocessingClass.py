from ReadDictClass import getDictList
from Lemmatization import lemmatization
import os
import re

conjunctionPath = os.getcwd() + "\\..\\Dictionaries\\conjunctions.txt"
prepositionPath = os.getcwd() + "\\..\\Dictionaries\\prepositions.txt"
particlePath = os.getcwd() + "\\..\\Dictionaries\\particles.txt"
interjectionPath = os.getcwd() + "\\..\\Dictionaries\\interjections.txt"
pronounsPath = os.getcwd() + "\\..\\Dictionaries\\pronouns.txt"
punctuationPath = os.getcwd() + "\\..\\Dictionaries\\punctuationMarks.txt"


class TextProcessing:
    def __init__(self, text):
        if text == "" or type(text) is not str:
            raise Exception("Empty text or not string")
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
