import json


def generateFile(quoteList: list):
    with open('quotes.json', 'w', encoding='utf-8') as file:
        json.dump(quoteList, file, indent=4, ensure_ascii=False)
