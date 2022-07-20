from fastapi import FastAPI
from scraper import naver_scraper, danawa_scraper

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "five-data-scraper"}


@app.get("/ping")
async def ping():
    return {"message": "pong"}


@app.get("/data/")
async def data(type: str = "", code: int = 0):
    if type == "naver":
        return naver.naver_scraper(code)
    elif type == "danawa":
        return scraper.danawa_scraper(code)
    else:
        return {"message": "type is not valid"}
