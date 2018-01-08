import mysql.connector
import json
import collections
cnx = mysql.connector.connect(user='root', password='mahendra',
                              host='127.0.0.1',
                              database='BookFinder')
cursor = cnx.cursor()

# query = ("INSERT INTO Colleges(CollegeName) VALUES('University of Kentucky')")

#dbName = "BookFinder"
# query = ("INSERT INTO Messages(User1, User2, Content) VALUES(3, 4, 'COnetemtmn')")
# query_data = ()
# cursor.execute(query)

'''
query = ("SELECT * FROM Users")
cursor.execute(query)
for (UID, FirstName, LastName, Email, PassWord, CollegeID) in cursor:
   print("{} {} {} {} {} {}".format(
     UID, FirstName, LastName, Email, PassWord, CollegeID))
'''
# users api

def userSignup(firstName, lastName, collegeId, email, passWord): #
    query = """INSERT INTO Users(FirstName, LastName, Email, PassWord, CollegeID) VALUES(%s,%s,%s,%s,%s)"""
    #atable=

    cursor.execute(query, (firstName, lastName, email, passWord, collegeId))
    cnx.commit()

def userSignin(email, password):
    msg = ''
    try:
        query="""SELECT UID, FirstName, LastName, Email, CollegeID FROM Users WHERE Email = %s AND PassWord=%s"""
        cursor.execute(query, (email, password))
        msg = 'Welcome!'
       # return "Welcome!"
    except mysql.connector.Error as err:
        msg = err

    return msg

def usersApi():
    query = ("SELECT UID, FirstName, LastName, Email, CollegeID  FROM Users")
    cursor.execute(query)
    rows = cursor.fetchall()
    rowArray_list = []
    #print (rows)
    #for row in rows:
    for i in range (len(rows)):
        t ={
           "UID": (rows[i][0]),
            "FirstName" :rows[i][1],
            "LastName" :rows[i][2],
            "Email" :rows[i][3],
            "CollegeID" :rows[i][4]
        }
        rowArray_list.append(t)

    j = json.dumps(rowArray_list)
    return ( j)

# College detail api
def collegeApi():
    query = ("SELECT CID, CollegeName  FROM Colleges")
    cursor.execute(query)
    rows = cursor.fetchall()

    rowArray_list = []
    #print (rows)
    #for row in rows:
    for i in range (len(rows)):
        t ={
           "CID": (rows[i][0]),
            "CollegeName":rows[i][1]
        }
        rowArray_list.append(t)

    j = json.dumps(rowArray_list)
    rowArrays_file = 'colleges.js'
    f = open(rowArrays_file,'w')
    f.write(j)
   # print (f, j)

def messageApi():
    query = ("SELECT MID, User1, User2, Content FROM Messages")
    cursor.execute(query)
    rows = cursor.fetchall()

    rowArray_list = []
    # print (rows)
    # for row in rows:
    for i in range(len(rows)):
        t = {
            "MID": (rows[i][0]),
            "User1": rows[i][1],
            "User2": rows[i][2],
            "Content": rows[i][3]
        }
        rowArray_list.append(t)

    j = json.dumps(rowArray_list)
    rowArrays_file = 'message.js'
    f = open(rowArrays_file, 'w')
    f.write(j)
    # print (f, j)

def listingApi():
    query = ("SELECT * FROM Listing")
    cursor.execute(query)
    rows = cursor.fetchall()

    rowArray_list = []
    # print (rows)
    # for row in rows:
    for i in range(len(rows)):
        t = {
            "LID": (rows[i][0]),
            "UserID": rows[i][1],
            "CollegeID": rows[i][2],
            "BookTitle": rows[i][3],
            "ISBN": rows[i][4],
            "Price": rows[i][5],
            "Description": rows[i][6]
        }
        rowArray_list.append(t)

    j = json.dumps(rowArray_list)
    rowArrays_file = 'listing.js'
    f = open(rowArrays_file, 'w')
    f.write(j)
    print (f, j)

def listingByUserApi(uid, reqType):
    if reqType == 'GET':
        query = ("SELECT * FROM Listing WHERE UserID = "+str(uid))
        cursor.execute(query)
        rows = cursor.fetchall()
        rowArray_list = []
        # print (rows)
        # for row in rows:
        for i in range(len(rows)):
            t = {
                "LID": (rows[i][0]),
                "UserID": rows[i][1],
                "CollegeID": rows[i][2],
                "BookTitle": rows[i][3],
                "ISBN": rows[i][4],
                "Price": float(rows[i][5]),
                "Description": rows[i][6]
            }
            rowArray_list.append(t)

        j = json.dumps(rowArray_list)

        return ( j)

    elif reqType == 'PUT':

        return "test put"


def listingByCollegeApi(cid, reqType):
    if reqType == 'GET':
        query = ("SELECT * FROM Listing WHERE CollegeID = "+str(cid))
        cursor.execute(query)
        rows = cursor.fetchall()
        rowArray_list = []
        # print (rows)
        # for row in rows:
        for i in range(len(rows)):
            t = {
                "LID": (rows[i][0]),
                "UserID": rows[i][1],
                "CollegeID": rows[i][2],
                "BookTitle": rows[i][3],
                "ISBN": rows[i][4],
                "Price": float(rows[i][5]),
                "Description": rows[i][6]
            }
            rowArray_list.append(t)

        j = json.dumps(rowArray_list)
        return (j)

    elif reqType == 'PUT':

        return "test put"

def main():
    # userSignup(firstName, lastName, collegeId, email, passWord)
    # usersApi()
    # collegeApi()
    # messageApi()
    # listingApi()
    # listingByUserApi(4)
    cursor.close()
    cnx.close()
    main()

if __name__ == "__main__":
    main()