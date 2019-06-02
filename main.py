import requests
import followStatistics
from bs4 import BeautifulSoup

#result = requests.get("https://twitter.com/JSourivongs")
#content = result.content
class Followstats:
    following=False
    followsYou=False
    def follows_you():
        return followsYou
    def following():
        return following

stats = dict()
followers = open("followers.html")
following = open('following.html')

followers_soup = BeautifulSoup(followers, features="html.parser")
following_soup = BeautifulSoup(following, features="html.parser")

followers = followers_soup.find_all("a", class_="FPmhX")
following = following_soup.find_all("a", class_="FPmhX")

for follower in followers:
    #print(follower.string)
    status=Followstats()
    status.follows_you = True
    status.following = False
    stats[follower.string]=status

for following in following:
    #print(follower.string)
    if following.string not in stats:
        status=Followstats()
        status.following = True
        status.follows_you = False
        stats[following.string]=status
    else:
        stats[following.string].following = True

it = iter(stats)
for u in it:
    user = stats[u]
    #if user.follows_you and user.following:
        #print(u.string + " and you follow each other!")
    #elif user.following:
        #print(u + " does not follow you back!")
    #else:
        #print(u + " is not followed back by you!")

julian = followStatistics.FollowStatistics()
julian.initTheRest("following.html", "followers.html")
#it = iter(julian.dontFollowBack)
it = iter(julian.doesntFollowYou)
for f in it:
    print(f)
