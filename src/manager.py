from typing import Counter
from requestManager import getQuoteList
from jsonManager import cleanAttributes, deleteRepeated
from fileManager import generateFile, readFile
from quoteClassificator import assignCategory

NUMBER_QUOTES: int = 5000
NUMBER_ITERATIONS: int = NUMBER_QUOTES // 50


def scrapeQuotes():
    quotes = []
    for iteration in range(1, NUMBER_ITERATIONS+1):
        jsonRequest = getQuoteList()
        jsonData = cleanAttributes(jsonRequest)
        quotes += jsonData
        percentage = (iteration / NUMBER_ITERATIONS) * 100
        print(f'\rProgress: {percentage:.2f}%', end='')
    generateFile(quotes, 'raw.json')
    print('\nProcessing complete!')


def categorizeQuotes():
    file = readFile('raw.json')
    jsonData = deleteRepeated(file)
    categorizedData = assignCategory(jsonData)
    generateFile(categorizedData, 'quotes.json')

    count = Counter(quote["category"] for quote in categorizedData)
    print(count)
