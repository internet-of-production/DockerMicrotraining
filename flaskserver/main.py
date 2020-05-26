import random
import os
from flask import Flask
from flask import request
from pymongo import MongoClient
app = Flask(__name__)

MONGOHOST = os.getenv("MONGOHOST", "127.0.0.1")
MONGOPORT = os.getenv("MONGOPORT", "27017")


ID = random.randint(0,1000000)
print(ID)

@app.route('/')
def getHome():
    return "<h1 style='color: red;'>HELLO IOP!</h1>"

@app.route('/getID')
def getID():
    return str(ID)

@app.route('/saveJson', methods = ['POST'])
def saveJson():
    content = request.get_json()
    print(content)
    print("Connecting to MongoDB")
    client = MongoClient(MONGOHOST, int(MONGOPORT))
    db = client.test_database
    posts = db.posts
    print("Inserting Datapoint")
    post_id = posts.insert_one(content).inserted_id
    return str(post_id)

@app.route('/getJson', methods = ['GET'])
def getJson():
    client = MongoClient(MONGOHOST, int(MONGOPORT))
    db = client.test_database
    collection = db.posts
    cursor = collection.find({})
    data = []
    for i in cursor:
        print(i)
        data.append(i)
    return str(data)+ "\n"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)
