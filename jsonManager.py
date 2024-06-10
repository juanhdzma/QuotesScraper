def cleanAttributes(quoteList: list):
    for quote in quoteList:
        quote['id'] = quote.pop('_id')
        del quote["tags"]
        del quote["authorSlug"]
        del quote["length"]
        del quote["dateAdded"]
        del quote["dateModified"]
    return quoteList
