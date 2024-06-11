import uuid


def cleanAttributes(quoteList: list):
    for quote in quoteList:
        quote['id'] = quote.pop('_id')
        del quote["tags"]
        del quote["authorSlug"]
        del quote["length"]
        del quote["dateAdded"]
        del quote["dateModified"]
    return quoteList


def deleteRepeated(quoteList: list):
    unique_data_dict = {item['id']: item for item in quoteList}
    return list(unique_data_dict.values())


def changeID(quoteList: list):
    for quote in quoteList:
        newID = str(uuid.uuid5(uuid.NAMESPACE_DNS, quote["content"]))
        quote["id"] = newID
    return quoteList
