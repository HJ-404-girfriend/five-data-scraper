// prod_tit : 상품명

// lwst_prc : 최저가 (현금도 있는데 알잘딱해야됨)

// ratingValue: 평점

// reviewCount: 평가자 수

// 	//다나와 페이지 데이터
// 	c.JSON(200, gin.H{
// 		"name":        "로지텍 MK270r (정품) (키스킨 미포함)",
// 		"price":       29700,
// 		"url":         "https://prod.danawa.com/info/?pcode=2541329",
// 		"rating":      4.6,
// 		"rater":       6683,
// 	})

package main

import (
	"fmt"
	"log"

	"github.com/antchfx/htmlquery"
	"github.com/antchfx/jsonquery"
)

// type aggregateRating struct {
// 	Rating int `json:"ratingValue"`
// 	Rater  int `json:"reviewCount"`
// }

// type offers struct {
// 	Price int `json:"lowPrice"`
// }

// type danawaWrap struct {
// 	Name            string `json:"name"`
// 	aggregateRating `json:"aggregateRating"`
// }

func main() {
	doc, err := htmlquery.LoadURL("https://prod.danawa.com/info/?pcode=2541329")
	if err != nil {
		log.Fatal(err)
	}

	rating := htmlquery.InnerText(htmlquery.FindOne(doc, "//*[@id='danawa_wrap']/script[46]"))
	fmt.Println(rating)
	doc, err := jsonquery.Parse(rating)
	if err != nil {
		panic(err)
	}
}
