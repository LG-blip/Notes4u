

# This file is to convert mongoDB key value pairs into python dictionaries.


# In the routes the note is inserted onto the database from this model "notesEntity"
# notesEntity return the list of items

def noteEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "title": item["title"],
        "desc": item["desc"],
        "important": item["important"]
    }


def notesEntity(items) -> list:
    return [noteEntity(item) for item in items]