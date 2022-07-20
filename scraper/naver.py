import requests
from bs4 import BeautifulSoup as bs


def naver_scraper(code):
    url = "https://search.shopping.naver.com/catalog/"

    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})

    page = requests.get(url + str(code), headers=HEADERS)

    soup = bs(page.text, "html.parser")

    name = soup.select_one(
        "#__next > div > div.style_container__3iYev > div.style_inner__1Eo2z > div.top_summary_title__15yAr > h2").get_text()

    imageUrl = soup.select_one(
        "#__next > div > div.style_container__3iYev > div.style_inner__1Eo2z > div.style_content_wrap__2VTVx > div.style_content__36DCX > div > div.image_thumb_area__1dzNx > div.image_photo_area__44Fqz > div > img")["src"]

    rating = soup.select_one(
        "#section_review > div.totalArea_total_area__NRExb > div.totalArea_graph_area__2tt4S > div:nth-child(1) > div.totalArea_average__TwE-s > div.totalArea_value__3UEUi").get_text()[:3]

    rater = soup.select_one(
        "#section_review > div.totalArea_total_area__NRExb > div.totalArea_graph_area__2tt4S > div:nth-child(2) > div > div").get_text().replace(",", "")

    price = soup.select_one(
        "#__next > div > div.style_container__3iYev > div.style_inner__1Eo2z > div.style_content_wrap__2VTVx > div.style_content__36DCX > div > div.summary_info_area__3XT5U > div.lowestPrice_price_area__OkxBK > div.lowestPrice_low_price__fByaG > em").get_text().replace(",", "")

    delivery = soup.select_one(
        "#__next > div > div.style_container__3iYev > div.style_inner__1Eo2z > div.style_content_wrap__2VTVx > div.style_content__36DCX > div > div.summary_info_area__3XT5U > div.lowestPrice_price_area__OkxBK > div.lowestPrice_delivery_price__3f-2l > em").get_text().replace(",", "")

    return {
        "name": name,
        "url": url + str(code),
        "imageUrl": imageUrl,
        "price": int(price),
        "delivery": int(delivery),
        "rating": rating,
        "rater": int(rater),
    }
