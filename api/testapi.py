#testapi.py?userid=1
from flask import Flask, request, render_template
app = Flask(__name__)

from api.user import *

@app.route('/api/usersignup', methods=['POST'])
def signupUser():
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    collegeId = request.form['collegeID']
    email = request.form['email']
    passWord = request.form['psw']
    return userSignup(firstName, lastName, collegeId, email, passWord)

@app.route('/api/usersignin', methods=['POST'])
def signInUser():
    email = request.form['email']
    passWord = request.form['psw']
    return userSignin(email, passWord)

@app.route('/api/listingbyuser', methods=['GET'])
def LBUA():
    userid= request.args.get('UID')
    reqType = 'GET'
    return listingByUserApi(userid, reqType)

@app.route('/api/listingbyuser', methods=['PUT'])
def putLBUA():
    userid= request.args.get('UID')
    reqType = 'PUT'
    return listingByUserApi(userid, reqType)


@app.route('/api/listingbycollegeid', methods=['GET'])
def listingBycollegeApi():
    collegeId= request.args.get('CID')
    reqType = 'GET'
    return listingByCollegeApi(collegeId, reqType)

@app.route('/api/usersapi')
def userAPIs():
    return usersApi()

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
