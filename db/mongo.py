from pymongo import MongoClient
from decouple import config


class MongoDB:
    def __init__(self, database_name=None, collection_name=None):
        self.client = MongoClient(config('DATABASE_URL'))
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def save(self, doc={}):
        self.collection.insert_one(doc)
