# TextPreprocessingAndShingleAlgorithm

## Description

This programme is created for text normalization in order to prepare the text for search of text borrowings.

It deletes stop words in input text

## API

```from TextProcessingClass import TextProcessing``` - import TextProcessing

```TextProcessing(text)``` - constructor receives input text

```TextProcessing.processText() -> string``` - returns result text without stop words

## Examples

**Taking text from file in *utf-8***

```
from TextProcessingClass import TextProcessing
import codecs

path = "C:\\Users\\kshir\\Desktop\\Text.txt"
file = codecs.open(path, encoding='utf-8')

Text = TextProcessing(file.read())
file.close()
print(Text.processText())
```

**Taking text from client code**

```
from TextProcessingClass import TextProcessing
Text = TextProcessing("Hello world!")
print(Text.processText())
```

## Notes

Dictionary files are located in *Dictionaries* directory

