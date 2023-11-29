import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        "http://quotes.toscrape.com/"
    ]

    # def parse(self, response):
    #     title = response.css('title ::text').extract()
    #     yield {'title': title}

#in terminal - scrapy shell "site add to scrap"

    def parse(self, response):
        all_div_quotes = response.css("div.quote")
        for quote in all_div_quotes:
            title = quote.css("span.text::text").extract()
            author = quote.css(".author::text").extract()
            tags = quote.css(".tag::text").extract()
            yield{
                "title":title,
                "author":author,
                "tags":tags
            }