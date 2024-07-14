from flask import Flask,request
from db import collection
import hashlib
app = Flask(__name__)


@app.route('/')
def home():
    return "Home"



@app.route('/auth/register', methods=('GET', 'POST'))
def register():

    if request.method =='POST':
        user =request.form["username"]
        psw =request.form["password"]
        hashed = hashlib.md5(psw.encode()).hexdigest()
        if collection.find_one({"username":user}):
            return {
                "message":"Exist"
            }
        else:
           collection.insert_one({"username":user,"password":hashed})
           return{
                "message":"Success",
                "username":user,
                "password":hashed

            }




@app.route('/auth/loggin', methods=('GET', 'POST'))
def loggin():

    if request.method =='POST':
        user =request.form["username"]
        psw =request.form["password"]
        hashed = hashlib.md5(psw.encode()).hexdigest()
        x = collection.find_one({"username":user}, {'_id': 0, 'username': 1, 'password': 1})
        if x:
           if x["password"]==hashed:
               
               return "ok"
           else:
               return "wrong"
        else:
          return "ko"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3001)