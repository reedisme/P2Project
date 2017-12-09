import pickle
import time
import sys


# Python mock social media website. We start by creating a user class
class User:
    """This Class defines a user in our domain."""

    def __init__(self, username, password):
        self.username = username
        self.password = password
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
        self.posts.append([post,[]])

# Storing our userbase and users to the pickle file 'data.pk.'
PIK = 'data.pk'


userbase = pickle.load( open( PIK, "rb" ))
#userbase = []

def quitprogram():
    pickle.dump(userbase, open(PIK, "wb"))
    sys.exit()

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
    username = input("Please input your username: \n")
    password = input("Please input your password: \n")
    uname, passwd = lookup(getObject(username))
    if passwd == password:
        for i in userbase:
            if username == i[1]:
                return i[0]
    else:
        print("Please try again")
        login()


def userGenerator():
    username = input("Please input a username: \n")
    if isuser(username) == False:
        password = input("Please input a password: \n")
        u = User(username, password)
        u.add_post("I just joined LeafMedia, and I could not be happier!")
        userbase.append((u, username, password))
    else:
        print("That username is taken. Please input a different username.")
        userGenerator()
    return u

def clear():
    for i in range(100):
        print(" ")

def commentOn(user, index):
    if type(index) is not int:
        print("Not integer")
    elif 0 < index and index <= len(user.posts):
        val = user.posts[index-1]
        print(val[0])
        print("\nComments:\n")
        if len(val[1]) > 0:
            for i in val[1][1:-1]:
                print(i, "\n\n")
        comment = str(input("Add your comment here: "))
        val[1].append(comment)
        print(val)


def home(user):
    if len(userbase)==1:
        print("There are no other users. Please sign up another user.")
        userGenerator()
    """Home function using user object."""
    print(userbase)
    print("Your friends:", user.friends)  # This section prints out the five most recent posts from your friends'
    if len(user.friends) == 0:
        print("You haven't added any friends yet! Here are some suggested users based on your area.")
        counter = 1
        for i in userbase:
            print(counter, i[1])
            counter += 1
        friendToAdd = str(input("Input a username to add them as your friend: \n"))
        while friendToAdd != str(0):
            if isuser(friendToAdd) == True:
                user.add_friend(getObject(friendToAdd))
                print(friendToAdd, "is now your friend!")
            else:
                print("This user does not exist.")
            friendToAdd = str(input("Input another friend, or input 0 to exit: \n"))
        home(user)
    else:
        clear()
        print("Recent posts from your friends! \n")
        for i in user.friends:
            username, probablynotapassword = lookup(i)
            print(username, "says:", i.posts[-1][0], "\n")
            if len(i.posts[-1][1]) > 0:
                print("    Comments:")
                for i in i.posts[-1][1]:
                    print("    " + i + "\n")
        action = str(input("Press 1 to add a new friend.\n"
                           "Press 2 to post.\n"
                           "Press 3 to view a friend's profile.\n"
                           "Press 4 to logout.\n"))
        if action == str(1):
            counter = 1
            for i in userbase:
                print(counter, i[1])
                counter += 1
            friendToAdd = str(input("Input a username to add them as your friend: \n"))
            while friendToAdd != str(0):
                if isuser(friendToAdd) == True:
                    user.add_friend(getObject(friendToAdd))
                    print(friendToAdd, "is now your friend!")
                else:
                    print("This user does not exist.")
                friendToAdd = str(input("Input another friend, or input 0 to exit: \n"))
            home(user)
        if action == str(2):
            mypost = str(input("What's on your mind? "))
            user.add_post(mypost)
        if action == str(3):
            print(user)
            for i in user.friends:
                friend, nothing = lookup(i)
                print(friend)
            friendToView = input("Please select a friends profile that you would like to view: \n")
            if isuser(friendToView) == True:
                print(friendToView + "'s profile:")
                counter = 0
                for i in getObject(friendToView).posts:
                    counter += 1
                    print(counter, i[0])
                post = int(input("Select which post you would like to comment on by pressing the corresponding number"
                                 ", or press 0 to exit.\n"))
                if post != 0:
                    commentOn(getObject(friendToView), post)
            else:
                print("Bad user")

        if action == str(4):
            clear()
            start = int(input("Welcome to LeafMedia!\n Press 1 to sign up.\n Press 2 to login.\n Press 3 to quit.\n"))
            main(start)
    home(user)

clear()
start = int(input("Welcome to LeafMedia!\n Press 1 to sign up.\n Press 2 to login.\n Press 3 to quit: \n"))

def main(s):
    if s == 1:
        u = userGenerator()
        home(u)
    elif s == 2:
        u = login()
        home(u)
    elif s == 3:
        quitprogram()


print(userbase)
main(start)