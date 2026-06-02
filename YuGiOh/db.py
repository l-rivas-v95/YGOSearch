from pymongo import MongoClient
from config import *

client = MongoClient(MONGO_URI)
cards_col = client[DB_NAME][CARDS_COLLECTION_NAME]
decks_col = client[DB_NAME][DECKS_COLLECTION_NAME]