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
        self.posts = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
            friend.friends.append(self)

    def remove_friend(self, friend):
        self.friends.remove(friend)
        friend.friends.remove(friend)

    def show_username(self):
        return self.username

    def show_friends(self):
        for i in self.friends:
            print(i.show_username())

    def clear_friends(self):
        self.friends = []

    def add_post(self, post):
        self.posts.append(post)

# Storing our userbase and users to the pickle file 'data.pk.'
PIK = 'data.pk'

with open(PIK, "rb") as f:
    objects = pickle.load(f)

userid, userbase = objects[0], objects[1]
#userid, userbase = 0, []

start = int(input("Welcome to LeaFacebook.\n Press 1 to sign up.\n Press 2 to login "))


def getObject(n):
    """Get id from username"""
    for i in userbase:
        if i[1] == str(n):
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
        password = input("Please input a password: ")
        userid += 1
        user = User(username, password, userid)
        user.add_post("I just joined LeafMedia, and I could not be happier!")
        userbase.append((user, username, password, userid))
    else:
        print("That username is taken. Please input a different username.")
        userGenerator()



def home(user):
    """Home function using user object."""
    print(userbase)
    print("Your friends:", user.friends)  # This section prints out the five most recent posts from your friends'
    if len(user.friends) == 0:
        print("You haven't added any friends yet! Here are some suggested users based on your area.")
        counter = 1
        for i in userbase:
            print(counter, i[1])
            counter += 1
        friendToAdd = str(input("Input a username to add them as your friend: "))
        while friendToAdd != str(0):
            if isuser(friendToAdd) == True:
                user.add_friend(getObject(friendToAdd))
                print(friendToAdd, "is now your friend!")
            else:
                print("This user does not exist.")
            friendToAdd = str(input("Input another friend, or input 0 to exit: "))
        home(user)
    else:
        for i in range(100):
            print(" ")
        print("Recent posts from your friends! \n")
        for i in user.friends:
            username, probablynotapassword = lookup(i)
            print(username, "says:", i.posts[-1], "\n")
        action = str(input("Press 1 to add a new friend, 2 to post, and 3 to view a friend's profile.\n"))
        if action == str(1):
            counter = 1
            for i in userbase:
                print(counter, i[1])
                counter += 1
            friendToAdd = str(input("Input a username to add them as your friend: "))
            while friendToAdd != str(0):
                if isuser(friendToAdd) == True:
                    user.add_friend(getObject(friendToAdd))
                    print(friendToAdd, "is now your friend!")
                else:
                    print("This user does not exist.")
                friendToAdd = str(input("Input another friend, or input 0 to exit: "))
            home(user)
        if action == str(2):
            mypost = input("What's on your mind?")
            user.posts.append(mypost)

    home(user)


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