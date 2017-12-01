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
        self.friends = []
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
    """Get id from username"""
    for i in userbase:
        if i[1] == n:
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
    if isuser(username) == False:
        userid += 1
        user = User(username, password, userid)
        userbase.append((user, username, password, userid))
    else:
        print("That username is taken. Please input a different username.")
        userGenerator()
    password = input("Please input a password: ")


def home(user):
    print("Recent posts from your friends!")  # This section prints out the five most recent posts from your friends
    tempposts = []
    allfriends = []
    for i in user.friends:
        allfriends.append(i.posthist[-1])
        allfriends.sort(reverse=True)
    for i in range(len(allfriends)):
        tempposts.append(allfriends[i])
    for i in tempposts:
        print(" ")
        print("Posted on " + time.gmtime(tempposts[0]) + ":")
        print(i[1])

    choice = input("Press 1 to make a new post, 2 to view a friend's profile, or 3 to log out.")
    if choice == 1:
        post = str(input("Enter the text of your new post here: "))
        user.posthist.append([int(time.time()), post])  # Clunky implementation! Time first so sorting is easy
        home(user)
    elif choice == 2:
        friend = eval(input("Whose profile would you like to see?"))  # Currently assuming this is the object ref.
        print("You are viewing " + friend.username + "'s profile:")
        print("User ID: " + friend.userid)
        print("Friends:")
        friend.show_friends()  # Currently we don't have any more profile info, but we can add it here if/when we do


def main(s):
    if s == 1:
        userGenerator()
    elif s == 2:
        u = login()
        home(u)


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