from xxlimited import Str
import requests
import json
from lxml import etree
from bs4 import BeautifulSoup as bs


def danawa_scraper(code):
    url = "https://prod.danawa.com/info/?pcode="

    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})

    page = requests.get(url + str(code), headers=HEADERS)

    soup = bs(page.text, "html.parser")
    dom = etree.HTML(str(soup))

    danawWrap = json.loads(
        dom.xpath("//*[@id='danawa_wrap']/script[46]")[0].text)

    delivery = soup.select_one(
        "#blog_content > div.summary_info > div.detail_summary > div.summary_left > div.lowest_area > div.lowest_list > table > tbody.card_list > tr > td.ship > span").get_text().replace(",", "").replace("원", "")

    return {
        "title": danawWrap["name"],
        "url": url + str(code),
        "imageUrl": "https://"+danawWrap["image"][0][2:],
        "price": int(danawWrap["offers"]["lowPrice"]),
        "delivery": int(delivery),
        "grade": danawWrap["aggregateRating"]["ratingValue"],
        "rater": int(danawWrap["aggregateRating"]["reviewCount"]),
    }
