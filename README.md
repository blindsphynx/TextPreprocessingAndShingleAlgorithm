# TextPreprocessingAndShingleAlgorithm

## Description

This programme compares two texts in order to find text borrowings in one of them and returns the result in percentage of borrowings.

Before comparing, texts are processed: they are normalized, divided into shingles and hashed.

## API

```from TextProcessingClass import TextProcessing``` - import TextProcessing

```TextProcessing(text)``` - constructor receives input text

```TextProcessing.processText() -> string``` - returns result text without stop words

```divideTextIntoShingles -> list``` - returns a list of hashed shingles

```compareTexts -> int``` - returns a percentage of the borrowed text

## Examples

**Taking two texts from files in *utf-8***

```
path1 = "..//test1.txt"
path2 = "..//test2.txt"
file1 = codecs.open(path1, encoding='utf-8')
file2 = codecs.open(path2, encoding='utf-8')
```

**Process two texts**

```
Text1 = divideTextIntoShingles(TextProcessing(file1.read()).processText())
Text2 = divideTextIntoShingles(TextProcessing(file2.read()).processText())
```

**Showing a percent of the borrowed text**

```
percent = compareTexts(Text1, Text2)
print('{}% of the text is borrowed'.format(percent))
```

## Notes

Dictionary files are located in *Dictionaries* directory

