from ReadDictClass import getDictList
import os

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

    def collectAllStopWords(self):
        allStopWords = set(getDictList(conjunctionPath, prepositionPath,
                                       interjectionPath, particlePath, pronounsPath))
        punctuationMarks = set(getDictList(punctuationPath))
        for sign in punctuationMarks:
            self._text = self._text.replace(sign, '')
        return allStopWords

    # TODO delete digits function

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
        return resultText
