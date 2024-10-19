import requests 
from bs4 import BeautifulSoup

def ScrapeModel(url):
    # list: ("alt": str, "src": str)
    content = []

    res = requests.get(url)
    soup = BeautifulSoup(res.content, "lxml")
    soup = soup.find("div", class_="story")
    for a in soup.find_all("p"):
        for i in a.find_all("img"):
            if i.get("alt") == "":
                continue
            alt = i.get("alt")
            print(f"alt: {alt}")
            src = i.get("src")
            print(f"src: {src}")
            content.append({"alt": alt, "src": src})

    return content