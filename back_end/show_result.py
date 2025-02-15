import pymongo

def find_result(ID, class_ID):
    collection = pymongo.MongoClient()["basicdb"][class_ID]
    result = collection.find_one({"_id": ID})
    print(result)
    