from TextPreprocessingClass import TextProcessing
from ShingleAlgorithm import divideTextIntoShingles
import codecs

path = "C:\\Users\\Lenovo\\Desktop\\Text.txt"
file = codecs.open(path, encoding='utf-8')

Text = TextProcessing(file.read())
file.close()
print(Text.processText())

# hashedText = Text.divideTextIntoShingles()
# print(hashedText)
