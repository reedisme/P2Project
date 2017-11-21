import pickle

class Graph:
    def __init__(self):
        self.matrix = {}

    def add_user(self, key):
        self.matrix[key] = []

    def add_friendship(self, v1, v2):
        if v1 in self.matrix and v2 in self.matrix:
            self.matrix[v1].append(v2)
            self.matrix[v1].sort()
        else:
            print("ERROR: One or both vertices do not yet exist")
        print(self.matrix)

    def is_edge(self, v1, v2):
        if v2 in self.matrix[v1]:
            return True
        else:
            return False

friendsdb = Graph()

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
        friendsdb.add_user(self.userid)

    def add_friend(self, friend):
        if self.userid > friend.userid:
            friendsdb.add_friendship(self.userid, friend.userid)
        elif friend.userid > self.userid:
            friendsdb.add_friendship(friend.userid, self.userid)

    def are_friends(self, friend):
        if self.userid > friend.userid:
            return friendsdb.is_edge(self.userid, friend.userid)
        elif friend.userid > self.userid:
            return friendsdb.is_edge(friend.userid, self.userid)

    def generate_flist(self):
        flist = []
        for i in friendsdb.matrix[self]:
            flist.append(i)
        for i in friendsdb.matrix:
            if self.userid in friendsdb.matrix[i]:
                flist.append(i)
        return(flist)

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
    global userid
    username = raw_input("Please input a username: ")
    password = raw_input("Please input a password: ")
    userid += 1
    user = User(username, password, userid)
    userbase.append((user, username, password, userid))
    return userbase

def main(s):
    if s == 1:
        userGenerator()
    elif s == 2:
        login()
print(userbase)
main(start)

saveObject = (userid, userbase)
with open(PIK,"wb") as f:
    pickle.dump(saveObject, f)

print(userbase[0][0].userid)
userbase[0][0].add_friend(userbase[1][0])
print(userbase[0][0].are_friends[userbase[1][0]])