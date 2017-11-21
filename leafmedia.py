import pickle
from itertools import count
#Pickle allows us to save our users in a separate file for easy access.

#Python mock social media website. We start by creating a user class
class User:
    """This Class defines a user in our domain."""
    def __init__(self, username, password):
        self.username  = username
        self.password  = password
        # self.first     = first
        # self.last      = last
        # self.birthday  = birthday
        self.friends   = []

    def add_friend(self, friend):
        self.friends.append(friend)

#Storing our userbase and users to the pickle file 'data.pk.'
PIK = 'data.pk'


with open(PIK, "rb") as f:
    objects = pickle.load(f)

users, userbase = objects[0], objects[1]
#users,userbase = 0, []

#TODO 2 to login.

start = int(input("Welcome to LeaFacebook.\n Press 1 to sign up.\n Press 2 to login "))
def getId(n):
    for i in userbase:
        if i[1] == n:
            return i[3]
    print("This is not a valid username")

def lookup(id):
    """Look up a persons username and password"""
    for i in userbase:
        if int(i[3]) == int(id):
            password = i[2]
            return password
    print("This is not a valid username")

def login():
    username = raw_input("Please input your username: ")
    password = raw_input("Please input your password: ")
    id = getId(username)
    passwd = lookup(id)
    if passwd == password:
        print("hooray")
    else:
        print("Please try again")
        login()

def userGenerator():
    global users
    username = raw_input("Please input a username: ")
    password = raw_input("Please input a password: ")
    user = User(username, password)
    users += 1
    userbase.append((user, username, password, users))
    return userbase

def main(s):
    print(userbase)
    if s == 1:
        userGenerator()
    elif s == 2:
        login()

main(start)

saveObject = (users, userbase)
with open(PIK,"wb") as f:
    pickle.dump(saveObject, f)