from requests import get

URL: str = 'https://api.quotable.io/quotes/random?tags=famous-quotes&limit=50'


def getQuoteList():
    response = get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")
