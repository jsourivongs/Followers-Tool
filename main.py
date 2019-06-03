import requests
import followStatistics
from bs4 import BeautifulSoup

#result = requests.get("https://twitter.com/JSourivongs")
#content = result.content

julian = followStatistics.FollowStatistics()
julian.initTheRest("following.html", "followers.html")
julian.printNoFBs()
