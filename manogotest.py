import pymongo
client = pymongo.MongoClient("mongodb+srv://eramitanand:eramitanand@cluster0.7roxj.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"amit",
    "email":"eramitanand@gmail.com",
    "surname":"kumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

