import scrapy


class ChocolatespiderSpider(scrapy.Spider):
    name = "chocolatespider"
    allowed_domains = ["chocolatescraper"]
    start_urls = ["https://chocolatescraper"]

    def parse(self, response):
        pass
