import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017")
print(myclient.list_database_names())
mydb = myclient["mydatabase"]  # creates database
mycol = mydb["customers"]  # creates collection

myquery = {"Address": "Mumbai"}
x = mycol.delete_many(myquery)
print(x.deleted_count, "Documents deleted")
