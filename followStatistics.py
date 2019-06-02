from bs4 import BeautifulSoup

class followStatistics:
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

    def initFollowing(path):
        f = open(path)
        soup = BeautifulSoup(f, features="html.parser")
        following = soup.find_all("a", class_="FPmhX")
        for u in following:
            user = u.string
            following[user]=true

    def initFollowers(path):
        f = open(path)
        soup = BeautifulSoup(f, features="html.parser")
        following = soup.find_all("a", class_="FPmhX")
        for u in following:
            user = u.string
            followers[user]=true
        return

    def initTheRest(followingPath, followersPath):
        initFollowing(followingPath)
        initFollowers(followersPath)
        for user in followers:
            if user in following:
                mutualFollowers[user]=True
            else:
                dontFollowBack[user] = True
        for user in following:
            if user not in mutualFollowers:
                doesntFollowYou[user] = True
