from ReadDictClass import getDictList
import os

conjunctionPath = os.getcwd() + "\\..\\Dictionaries\\conjunctions.txt"
prepositionPath = os.getcwd() + "\\..\\Dictionaries\\prepositions.txt"
particlePath = os.getcwd() + "\\..\\Dictionaries\\particles.txt"
interjectionPath = os.getcwd() + "\\..\\Dictionaries\\interjections.txt"
punctuationPath = os.getcwd() + "\\..\\Dictionaries\\punctuationMarks.txt"


class TextProcessing:
    def __init__(self, text):
        if text == "" or type(text) is not str:
            raise Exception("Empty text or not string")
        self._text = text

    def processText(self):
        setOfStopWords = set(getDictList(conjunctionPath, prepositionPath,
                             interjectionPath, particlePath))
        punctuationWords = set(getDictList(punctuationPath))
        for sign in punctuationWords:
            self._text = self._text.replace(sign, '')

        resultText = self._text.split(' ')
        for i in range(0, len(resultText)):
            if resultText[i].lower().replace('\r', '').replace('\n', '') in setOfStopWords:
                resultText[i] = ''
        return ' '.join([value for value in resultText if value != ''])