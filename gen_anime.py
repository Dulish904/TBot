from random import randint
import requests
from bs4 import BeautifulSoup


def img_gen():
    exempl = "https://www.thiswaifudoesnotexist.net/./example-"
    result = exempl + str(randint(1, 99999)) + ".jpg"

    return result

pz_url = "https://projectzomboid.com/blog/news/"
actual_news = ""
def pz_news():
    text_url = requests.get(pz_url).text
    soup = BeautifulSoup(text_url, "lxml")
    list_href = soup.find("div", class_="col-12 mb-5 col-lg-4")
    link_text = list_href.find("a")
    link = link_text.get('href')
    return link
print(pz_news())