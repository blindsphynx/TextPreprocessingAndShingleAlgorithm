from TextPreprocessingClass import TextProcessing
from ShingleAlgorithm import divideTextIntoShingles
from Compare import compareTexts
import codecs

for i in range(94):

    file1 = codecs.open(F"..//tests//текст{i}.txt", encoding='utf-8')
    file2 = codecs.open(F"..//tests//плагиат{i}.txt", encoding='utf-8')

    Text1 = divideTextIntoShingles(TextProcessing(file1.read()).processText())
    Text2 = divideTextIntoShingles(TextProcessing(file2.read()).processText())

    file1.close()
    file2.close()

    percent = compareTexts(Text1, Text2)
    print('{}% of the text is borrowed'.format(percent))
