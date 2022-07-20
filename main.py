import string
from fastapi import FastAPI
from scraper import naver, danawa

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "five-data-scraper"}


@app.get("/ping")
async def ping():
    return {"message": "pong"}


@app.get("/data/")
async def data(type: string = 0, code: int = 10):
    if type == "naver":
        return naver.naver_scraper(code)
    elif type == "danawa":
        return danawa.danawa_scraper(code)
    else:
        return {"message": "type is not valid"}
