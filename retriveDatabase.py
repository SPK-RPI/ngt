import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017")
print(myclient.list_database_names())

mydb = myclient["mydatabase"]
mycol = mydb["customers"]


for x in mycol.find():
    print(x)
