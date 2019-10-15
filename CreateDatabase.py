import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017")
print(myclient.list_database_names())
mydb = myclient["mydatabase"]  # creates database
mycol = mydb["customers"]  # creates collection
mydict = {"name": "ABC", "Address": "Mumbai"}
x = mycol.insert_one(mydict)  # insert document in collection
for x in mycol.find():
    print(x)
