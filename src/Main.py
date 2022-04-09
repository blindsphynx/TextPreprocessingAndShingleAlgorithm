from TextPreprocessingClass import TextProcessing
from ShingleAlgorithm import divideTextIntoShingles
from Compare import compareTexts
import codecs
import os

path1 = "..//test1.txt"
path2 = "..//test2.txt"
file1 = codecs.open(path1, encoding='utf-8')
file2 = codecs.open(path2, encoding='utf-8')

Text1 = divideTextIntoShingles(TextProcessing(file1.read()).processText())
Text2 = divideTextIntoShingles(TextProcessing(file2.read()).processText())

percent = compareTexts(Text1, Text2)
print('{}% of the text is borrowed'.format(percent))
