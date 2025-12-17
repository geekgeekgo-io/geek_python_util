
import os
from pymongo import MongoClient
class MongoDbUtil():
    def open_connection(self, connection_string, collection_name):
        client = MongoClient(connection_string)
        db = client[collection_name]
        return db

