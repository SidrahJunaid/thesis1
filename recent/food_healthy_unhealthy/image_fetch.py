from bs4 import BeautifulSoup
import requests
import urllib.request
data =  requests.get("https://t.co/KXrcEQlkYI").text

soup = BeautifulSoup(data, "html.parser")

#array of tags
img_data = soup.find_all("div", {"class": "AdaptiveMedia-photoContainer"})

for i in img_data:
  #saving images
  i  = i.find("img")['src']
  urllib.request.urlretrieve(i, i.replace("https://pbs.twimg.com/media/", ""))