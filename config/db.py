

# database connection is defined here


from pymongo import MongoClient

MONGO_URI = "mongodb+srv://lgnotesapp:<password>@notes.wr0ndq5.mongodb.net/"

conn = MongoClient(MONGO_URI)
