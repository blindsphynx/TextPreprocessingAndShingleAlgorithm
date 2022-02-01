from TextPreprocessingClass import TextProcessing
from ShingleAlgorithm import divideTextIntoShingles
import codecs

path = "C:\\Users\\Lenovo\\Desktop\\digits.txt"
file = codecs.open(path, encoding='utf-8')

Text = TextProcessing(file.read())
print(Text.processText())
# Text = TextProcessing(file.read()).processText()
file.close()
# print(divideTextIntoShingles(Text))
