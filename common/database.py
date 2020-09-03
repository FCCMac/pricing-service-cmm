import pymongo
import json
import os
import sys


class Database(object):
    URI = "mongodb+srv://{}:{}@cluster0.sfoyz.mongodb.net/<dbname>?retryWrites=true&w=majority"
    DATABASE = None

    @staticmethod
    def initialize(): 
        db = 'pricing'
        Database.URI = os.environ.get('DB_URI')

        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client[db]

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def update(collection, query, data):
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection, query):
        return Database.DATABASE[collection].remove(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
