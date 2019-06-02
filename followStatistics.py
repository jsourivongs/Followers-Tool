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
    def numFollowers():
        return numFollowers

    def numFollowing():
        return numFollowing

    def printMutuals():
        print("Not yet implemented")

    def initFollowing(self, path):
        f = open(path)
        soup = BeautifulSoup(f, features="html.parser")
        following = soup.find_all("a", class_="FPmhX")
        for u in following:
            user = u.string
            self.following[user]=True

    def initFollowers(self, path):
        f = open(path)
        soup = BeautifulSoup(f, features="html.parser")
        following = soup.find_all("a", class_="FPmhX")
        for u in following:
            user = u.string
            self.followers[user]=True
        return

    def initTheRest(self, followingPath, followersPath):
        self.initFollowing(followingPath)
        self.initFollowers(followersPath)
        for user in self.followers:
            if user in self.following:
                self.mutualFollowers[user]=True
            else:
                self.dontFollowBack[user] = True
        for user in self.following:
            if user not in self.mutualFollowers:
                self.doesntFollowYou[user] = True
