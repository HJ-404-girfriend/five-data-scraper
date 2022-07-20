package main

import (
	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()

	router.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})

	// Get product information
	router.GET("/data", scraper)
	// router.HEAD("/data", scraperHead)
	router.Run(":4001")
}
h