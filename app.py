from flask import Flask, render_template, jsonify, request, Response, redirect, url_for, make_response
import os
import json

DEBUG = bool(os.getenv('DEBUG', False))

app = Flask(__name__)


@app.route('/users', methods = ['GET','POST'])
def index():
    if request.method == "POST":
        user = request.json
        users={}
        with open('users.json') as f:
            users = json.loads(f.read())
  
            
            
        with open('users.json', 'w') as f:
            userName=user["name"]
            del user["name"]
            users[userName]=user
            f.write(json.dumps(users))
            return Response(status=201)
            

           

    elif request.method == "GET":
        with open('users.json') as f:
            users = json.loads(f.read())
            user = request.json
            print(user)
            return jsonify(users)


@app.route('/hello/')
def hello1():
    return render_template('hello.html', title="Custom title")


@app.route('/hello2/')
def hello2():
    return render_template('hello2.html')


@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', fullname=name)

@app.route('/create/', methods = ['POST'])
def createUsers():
    user = request.json
    print(user)
    with open('users.json', 'w') as f:
        f.write(json.dumps(user))
    return Response(status=201)

adminList = ["1", True]

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    elif request.method == 'POST':
        with open('users.json') as f:
            users = json.loads(f.read())
            userName = request.form['un']
            passWord= request.form['pw']
            if userName in users and users[userName]["password"] == passWord and users[userName]["admin"] in adminList:
                money = str(users[userName]["money"])
                resp = make_response(render_template('admin.html', message="Nå er du logget inn som admin!"))
                resp.set_cookie('money', money)    
                return resp

            elif userName in users and users[userName]["password"] == passWord and users[userName]["admin"] not in adminList:
                money = str(users[userName]["money"])
                resp = make_response(render_template('user.html', message="You are a user!"))
                resp.set_cookie('money', money)    
                return resp



            #resp = make_response(render_template('readcookie.html'))
            #resp.set_cookie('userID', user)
            #if userName == "admin" and passWord == "dickbutt":
                #return render_template('admin.html', message="You are a hacker!")

            else:
                return render_template('login.html', message="Wrong username/password!")
                
    
        

    


@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == "POST":
        users = {}
        with open('users.json') as f:
            users = json.loads(f.read())

        userName = request.form['un']
        passWord= request.form['pw']
        passWordRep = request.form['pw2']
        #sjekke om brukernavnet finnes fra før
        if userName in users:
            return render_template('register.html', message="Dette brukernavnet finnes fra før!")

        #sjekke om passordene er identiske
        if passWord != passWordRep:
            return render_template('register.html', message="Passordene stemmer ikke!")

        newUser = {
            "admin": request.form['admin'],
            "money": 0,
            "password": passWord
        }

        with open('users.json', 'w') as f:
            users[userName]=newUser
            f.write(json.dumps(users))
            return render_template('login.html', message="New user created successfully!")



    elif request.method == "GET":
        return render_template('register.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=DEBUG)

