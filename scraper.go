package main

import (
	"github.com/gin-gonic/gin"
)

func scraper(c *gin.Context) {

	//다나와 페이지 데이터
	c.JSON(200, gin.H{
		"name":        "로지텍 MK270r (정품) (키스킨 미포함)",
		"category":    "키보드",
		"price":       29700,
		"shippingFee": 2500,
		"url":         "https://prod.danawa.com/info/?pcode=2541329",
		"rating":      4.6,
		"rater":       6683,
	})

	//네이버 페이지 데이터
	c.JSON(200, gin.H{
		"name":        "QCY T13APP",
		"category":    "무선 이어폰",
		"price":       19520,
		"shippingFee": 3000,
		"url":         "https://search.shopping.naver.com/catalog/28473903554",
		"rating":      4.8,
		"rater":       17668,
	})
}
