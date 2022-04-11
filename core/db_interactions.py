from pymongo import MongoClient

client = MongoClient("mongodb+srv://business:doUeTyy8tulrIEI8@cluster0.vp1o3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["businesscord"]
users = db["users"]

def get_value(id, item):
    return users.find_one({"id": id})[item]
def get_all_values(id):
    return users.find_one({"id": id})
def check_if_exists(id):
    if users.find_one({"id": id}) is None:
        return False
    else:
        return True
def get_user(id):
    return users.find_one({"id": id})