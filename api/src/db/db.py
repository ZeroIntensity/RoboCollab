import pymongo
from utils import StateConfig

connection = pymongo.MongoClient(
    StateConfig["mongo_url"]
)
db = connection["robocollab"]
auth = db["auth"]
collabs = db["collabs"]