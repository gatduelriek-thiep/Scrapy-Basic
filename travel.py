import scrapy
class TravelScrapy(scrapy.Spider):
    name = "travel"
    start_urls = ["https://books.toscrape.com/catalogue/category/books/travel_2/index.html"]

    def parse(self, response):
        travels = response.css("article")

        for travel in travels:
            title = travel.css("h3 a::text").get()
            price = travel.css("p.price_color::text").get()


            yield{
                "Title": title, "Price":price
            }