import sys
from manager import scrapeQuotes, categorizeQuotes, regenerateID


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <task_name>")
        return

    task_name = sys.argv[1]
    if task_name == 'scrape':
        scrapeQuotes()
    elif task_name == 'categorize':
        categorizeQuotes()
    elif task_name == 'id':
        regenerateID()
    else:
        print("Not a valid task_name")
        return


if __name__ == "__main__":
    main()
