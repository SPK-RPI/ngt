import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017")
print(myclient.list_database_names())
mydb = myclient["mydatabase"]  # creates database
mycol = mydb["customers"]  # creates collection
mylist = [{"name": "ABC", "Address": "Mumbai"},
          {"name": "XYZ", "Address": "Thane"}]
x = mycol.insert_many(mylist)  # insert document in collection
for x in mycol.find():
    print(x)
