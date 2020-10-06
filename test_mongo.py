import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["students"]
mydict = {"name":"rohan", "age": 30, "loc": "blr"}
# data = mycol.insert_one(mydict)
# mycol.delete_one(mydict)
for i in mycol.find():
    print(i)