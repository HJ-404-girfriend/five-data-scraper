import requests
import json
from lxml import etree
from bs4 import BeautifulSoup as bs

code = "2541329"
url = "https://prod.danawa.com/info/?pcode="

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

page = requests.get(url + code, headers=HEADERS)

soup = bs(page.text, "html.parser")
dom = etree.HTML(str(soup))

danawWrap = json.loads(
    dom.xpath("//*[@id='danawa_wrap']/script[46]")[0].text)

returnData = {
    "name": danawWrap["name"],
    "url": danawWrap["offers"]["url"],
    "imageUrl": danawWrap["image"][0][2:],
    "price": danawWrap["offers"]["lowPrice"],
    "rating": danawWrap["aggregateRating"]["ratingValue"],
    "rater": danawWrap["aggregateRating"]["reviewCount"],
}

print(returnData)
