from fastapi import FastAPI
from scraper import naver_scraper, danawa_scraper
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "five-data-scraper"}


@app.get("/ping")
async def ping():
    return {"message": "pong"}


@app.get("/api/data/")
async def data(type: str = "", code: int = 0):
    if type == "naver":
        return naver_scraper(code)
    elif type == "danawa":
        return danawa_scraper(code)
    else:
        return {"message": "type is not valid"}
