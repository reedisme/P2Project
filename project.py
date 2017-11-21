import pickle
#Pickle allows us to save our users in a separate file for easy access.

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
    userid = 0

    def __init__(self, first, last):
        self.first     = first
        self.last      = last
        # self.birthday  = birthday
        self.friends   = []
        User.userid += 1
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

#Storing our userbase to the pickle file 'data.pk.'
data = 'data.pk'
userbase = pickle.load( open( data, 'rb' ) )

#TODO 2 to login.

# start = int(input("Welcome to LeaFacebook. Press 1 to sign up."))

def userGenerator():
    firstname = input("Please input your first name: ")
    lastname = input("Please input your last name: ")
    user = User(firstname, lastname)
    userbase.append((user, user.userid, user.first))

# userGenerator()
# print(userbase)

pickle.dump( userbase, open( data, 'wb' ) )
userbase[0][0].add_friend(userbase[1][0])
print(userbase[0][0].are_friends(userbase[1][0]))