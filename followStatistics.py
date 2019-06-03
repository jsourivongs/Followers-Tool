from bs4 import BeautifulSoup

class FollowStatistics:
    # Member Variables
    numFollowers=0
    numFollowing=0
    followers=dict()
    following=dict()
    mutualFollowers=dict()
    dontFollowBack=dict()
    doesntFollowYou=dict()

    # Functions
    def printMutuals(self):
        mutuals = iter(self.mutualFollowers)
        for user in mutuals:
            print(user)
        return

    def printNoFBs(self):
        nonFB = iter(self.doesntFollowYou)
        for user in nonFB:
            print(user)
        return

    def printUsers(self, userDict):
        users = iter(userDict)
        for user in users:
            print(user)
        return

    def _initFollowing(self, path):
        f = open(path)
        soup = BeautifulSoup(f, features="html.parser")
        following = soup.find_all("a", class_="FPmhX")
        for u in following:
            user = u.string
            self.following[user]=True
            self.numFollowing += 1
        return

    def _initFollowers(self, path):
        f = open(path)
        soup = BeautifulSoup(f, features="html.parser")
        following = soup.find_all("a", class_="FPmhX")
        for u in following:
            user = u.string
            self.followers[user]=True
            self.numFollowers += 1
        return

    def initTheRest(self, followingPath, followersPath):
        self._initFollowing(followingPath)
        self._initFollowers(followersPath)
        for user in self.followers:
            if user in self.following:
                self.mutualFollowers[user]=True
            else:
                self.dontFollowBack[user] = True
        for user in self.following:
            if user not in self.mutualFollowers:
                self.doesntFollowYou[user] = True
