import scrapy
import pandas as pd
import time
import random

df = pd.read_excel(r"C:\Users\nirma\Downloads\albion casters urls.xlsx")

class QuoteSpider(scrapy.Spider):
    name = 'raju'
    start_urls = [url for url in df['ORI'][:2000]]

    def __init__(self):
        self.scraped_data_list = []

    def parse(self, response):
        # Add a random delay between 2 to 5 seconds
        time.sleep(random.uniform(2, 5))

        part_number1 = response.css("div.prod-sku")
        part_number = part_number1.css("h2::text").extract_first()

        series1 = response.css("div.series-name")
        series = series1.css("a::text").extract_first()

        des = response.css("div.product-description::text").extract_first()

        image = response.css("div.prod-image img::attr(src)").extract_first()

        technical_data = response.css("div#technical-data p.attribute-row")
        attributes = {}

        for row in technical_data:
            name = row.css("span.attribute-name::text").extract_first().strip()
            value = row.css("span.attribute-value::text").extract_first().strip()
            attributes[name] = value

        datasheet_link = response.css("a[title='Download Datasheet']::attr(href)").extract_first()

        scraped_data = {
            "ORI": response.url,
            "status": response.status,
            "part_number": part_number,
            "series": series,
            "description": des,
            "image": image,
            "technical_data": attributes,
            "datasheet_link": datasheet_link,
        }

        self.scraped_data_list.append(scraped_data)

        # Continue with the rest of your parsing logic

    def closed(self, reason):
        # Create a DataFrame from the list of scraped data
        df = pd.DataFrame(self.scraped_data_list)

        # Save the DataFrame to a CSV file
        df.to_csv('nkr_albion_caster_data.csv', index=False)
