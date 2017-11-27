import pickle
#Python mock social media website. We start by creating a user class
class User:
    """This Class defines a user in our domain."""

    def __init__(self, username, password, userid):
        self.username  = username
        self.password  = password
        self.userid    = userid
        # self.first     = first
        # self.last      = last
        # self.birthday  = birthday
        self.friends   = []

    def add_friend(self, friend):
        self.friends.append(friend)

    def show_username(self):
        return self.username

    def show_friends(self):
        for i in self.friends:
            print(i.show_username())

#Storing our userbase and users to the pickle file 'data.pk.'
PIK = 'data.pk'

with open(PIK, "rb") as f:
    objects = pickle.load(f)

userid, userbase = objects[0], objects[1]
#userid, userbase = 0, []

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
    username = input("Please input your username: ")
    password = input("Please input your password: ")
    id = getId(username)
    passwd = lookup(id)
    if passwd == password:
        for i in userbase:
            if username == i[1]:
                return i[0]
    else:
        print("Please try again")
        login()

def userGenerator():
    global userid
    username = input("Please input a username: ")
    password = input("Please input a password: ")
    userid += 1
    user = User(username, password, userid)
    userbase.append((user, username, password, userid))
    return userbase

def home():
    for i in range(100):
        print(" ")

def main(s):
    if s == 1:
        userGenerator()
    elif s == 2:
        login()
        home()

main(start)

saveObject = (userid, userbase)
with open(PIK,"wb") as f:
    pickle.dump(saveObject, f)

# print(userbase[0][0].username)
userbase[0][0].add_friend(userbase[1][0])
userbase[0][0].add_friend(userbase[2][0])
userbase[0][0].add_friend(userbase[3][0])
userbase[0][0].show_friends()
