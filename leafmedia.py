import pickle
#Pickle allows us to save our users in a separate file for easy access.

#Python mock social media website. We start by creating a user class
class User:
    """This Class defines a user in our domain."""
    userid = 0

    def __init__(self, first, last):
        self.first     = first
        self.last      = last
        # self.birthday  = birthday
        self.friends   = []
        User.userid += 1

    def add_friend(self, friend):
        self.friends.append(friend)

#Storing our userbase to the pickle file 'data.pk.'
data = 'data.pk'
userbase = pickle.load( open( data, 'rb' ) )

#TODO 2 to login.

start = int(input("Welcome to LeaFacebook. Press 1 to sign up."))

def userGenerator():
    firstname = input("Please input your first name: ")
    lastname = input("Please input your last name: ")
    user = User(firstname, lastname)
    userbase.append((user, user.userid, user.first))

userGenerator()
print(userbase)

pickle.dump( userbase, open( data, 'wb' ) )
