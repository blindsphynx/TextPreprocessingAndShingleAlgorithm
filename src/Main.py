from TextPreprocessingClass import TextProcessing
from ShingleAlgorithm import divideTextIntoShingles
import codecs

path = "C:\\Users\\Lenovo\\Desktop\\Text.txt"
file = codecs.open(path, encoding='utf-8')

# print(Text.processText())
Text = TextProcessing(file.read()).processText()
file.close
# print(len(Text))
print(divideTextIntoShingles(Text))
