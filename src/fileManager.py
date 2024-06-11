import json


def generateFile(quoteList: list, fileName: str):
    with open(fileName, 'w', encoding='utf-8') as file:
        json.dump(quoteList, file, indent=4, ensure_ascii=False)


def readFile(fileName: str):
    with open(fileName, 'r', encoding='utf-8') as file:
        return json.load(file)
