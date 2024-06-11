from transformers import pipeline

CATEGORIES = [
    "Motivation and Inspiration",
    "Love and Relationships",
    "Wisdom and Knowledge",
    "Life and Existence",
    "Society and Humanity"
]


def assignCategory(quoteList: list):
    classifier = pipeline("zero-shot-classification",
                          model="facebook/bart-large-mnli")
    TOTAL = len(quoteList)

    for index, quote in enumerate(quoteList):
        result = classifier(quote['content'], CATEGORIES)
        quote['category'] = result['labels'][0]
        percentage = ((index + 1) / TOTAL) * 100
        print(f'\rProgress: {percentage:.2f}%', end='')
    print('\nData categorized!')

    return quoteList
