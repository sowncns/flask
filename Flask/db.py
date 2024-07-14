from pymongo import MongoClient
uri = "mongodb+srv://abc:uZ6rgaOzYL5ABzVA@cluster0.8vbejcq.mongodb.net/?appName=Cluster0"

client = MongoClient(uri)
db = client['demo']
collection = db['data']
