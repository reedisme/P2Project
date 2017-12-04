import pickle
import time


# Python mock social media website. We start by creating a user class
class User:
    """This Class defines a user in our domain."""

    def __init__(self, username, password, userid):
        self.username = username
        self.password = password
        self.userid = userid
        # self.first     = first
        # self.last      = last
        # self.birthday  = birthday
        self.friends = []   # objects
        self.posthist = []

    def add_friend(self, friend):
        self.friends.append(friend)

    def show_username(self):
        return self.username

    def show_friends(self):
        for i in self.friends:
            print(i.show_username())


# Storing our userbase and users to the pickle file 'data.pk.'
PIK = 'data.pk'

with open(PIK, "rb") as f:
    objects = pickle.load(f)

userid, userbase = objects[0], objects[1]
# userid, userbase = 0, []

start = int(input("Welcome to LeaFacebook.\n Press 1 to sign up.\n Press 2 to login "))


def getObject(n):
    """Get object from username"""
    for i in userbase:
        print(i[1], n)
        if str(i[1]) == str(n):
            return i[0]
    print("This is not a valid username")


def lookup(obj):
    """Look up a persons username and password given user object"""
    for i in userbase:
        if i[0] == obj:
            return i[1], i[2]
    print("This is not a valid user")


def isuser(u):
    for i in userbase:
        if u == i[1]:
            return True
    return False


def login():
    username = str(input("Please input your username: "))
    password = str(input("Please input your password: "))
    uname, passwd = lookup(getObject(username))
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
    if isuser(username) == False:
        userid += 1
        user = User(username, password, userid)
        userbase.append((user, username, password, userid))
    else:
        print("That username is taken. Please input a different username.")
        userGenerator()
    password = input("Please input a password: ")


def home(user):
    print("Recent posts from your friends!")    # This section prints out the five most recent posts from your friends
    tempposts = []
    allfriends = []
    for i in getObject(user).friends:
        tempfriend = i
        print(tempfriend)
        allfriends.append(tempfriend.posthist[-1])
        allfriends.sort()
    for i in range(len(allfriends)):
        tempposts.append(allfriends.pop())
    for i in tempposts:
        print(" ")
        print("Posted on " + time.gmtime(tempposts[0]) + ":")
        print(i[1])

    choice = int(input("Press 1 to make a new post, 2 to view a friend's profile, 3 to add a friend, or 4 to log out."))
    if choice == 1:
        post = str(input("Enter the text of your new post here: "))
        getObject(user).posthist.append([int(time.time()), post])  # Clunky implementation! Time first so sorting is easy
        home(user)
    elif choice == 2:
        friend = eval(input("Whose profile would you like to see?"))
        print("You are viewing " + friend + "'s profile:")
        print("Friends:")
        getObject(friend).show_friends()   # Currently we don't have any more profile info, but we can add it here if/when we do
    elif choice == 3:
        friend = eval(input("Who would you like to add as a friend?"))
        user.add_friend(getObject(friend))
        # counter = 1
        # for i in userbase:
        #     print(counter, "   ", i[1])
        #     counter += 1
        # user.add_friend(input("Press the number corresponding to the new friend's username: "))


def main(s):
    if s == 1:
        userGenerator()
    elif s == 2:
        u = login()
        usr, pswd = lookup(u)
        home(usr)


print(userbase)
main(start)

saveObject = (userid, userbase)
with open(PIK, "wb") as f:
    pickle.dump(saveObject, f)

    # print(userbase[0][0].username)
    # userbase[0][0].add_friend(userbase[1][0])
    # userbase[0][0].add_friend(userbase[2][0])
    # userbase[0][0].add_friend(userbase[3][0])
    # userbase[0][0].show_friends()