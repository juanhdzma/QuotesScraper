from requestManager import getQuoteList
from jsonManager import cleanAttributes
from fileManager import generateFile

NUMBER_QUOTES: int = 20000
NUMBER_ITERATIONS: int = NUMBER_QUOTES // 50


def manageProcess():
    quotes = []
    for iteration in range(1, NUMBER_ITERATIONS+1):
        jsonRequest = getQuoteList()
        jsonData = cleanAttributes(jsonRequest)
        quotes += jsonData
        percentage = (iteration / NUMBER_ITERATIONS) * 100
        print(f'\rProgress: {percentage:.2f}%', end='')
    generateFile(quotes)
    print('\nProcessing complete!')


manageProcess()
