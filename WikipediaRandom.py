import requests
from bs4 import BeautifulSoup
import webbrowser
import time

mytable = None

while True:
    a = "https://en.wikipedia.org/wiki/Special:Random"
    u = requests.get(a)
    soup = BeautifulSoup(u.content, 'html.parser')
    title = soup.find(class_ = "firstHeading").text
    mytable = soup.find("table", class_ = "wikitable sortable")
    print("No tables on:" + " " + title + " " + "Wikipedia page")
    print("Continuing to search...")
    time.sleep(2)
    if mytable is not None:
        url = 'https://en.wikipedia.org/wiki/%s' %title
        webbrowser.open(url)
        print("Navigating")
        break
