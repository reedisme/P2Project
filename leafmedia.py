import pickle
from itertools import count
#Pickle allows us to save our users in a separate file for easy access.

#Python mock social media website. We start by creating a user class
class User:
    """This Class defines a user in our domain."""
    def __init__(self, first, last):
        self.first     = first
        self.last      = last
        # self.birthday  = birthday
        self.friends   = []

    def add_friend(self, friend):
        self.friends.append(friend)

#Storing our userbase and users to the pickle file 'data.pk.'
PIK = 'data.pk'


with open(PIK, "rb") as f:
    objects = pickle.load(f)

users, userbase = objects[0], objects[1]
#TODO 2 to login.

start = int(input("Welcome to LeaFacebook. Press 1 to sign up."))

def userGenerator():
    global users
    firstname = input("Please input your first name: ")
    lastname = input("Please input your last name: ")
    user = User(firstname, lastname)
    users += 1
    userbase.append((user, user.first, users))


userGenerator()
print(userbase)
print(users)

saveObject = (users, userbase)
with open(PIK,"wb") as f:
    pickle.dump(saveObject, f)