import scrapy
from chocolatescraper.items import ChocolateProduct
from chocolatescraper.itemloaders import ChocolateProductLoader
class ChocolatespiderSpider(scrapy.Spider):
    name = "chocolatespider"
    allowed_domains = ["chocolatescraper"]
    start_urls = ['https://www.chocolate.co.uk/collections/all']   

    def parse(self, response):
        products = response.css('.product-item')
        
        for product in products:
            chocolate = ChocolateProductLoader(item=ChocolateProduct(),selector=product)
            chocolate.add_css('name','div.product-item-meta a::text')
            chocolate.add_css('price','span.price',re=r'£\d+\.\d{2}')
            chocolate.add_css('url','div.product-item-meta a::attr(href)')
            if(product.css('div.product-item__image-wrapper div span::text').get()):
                chocolate.add_value('status','Out of Stock')
            else:
                chocolate.add_value('status','In Stock')
            yield chocolate.load_item()
            
        
        next_page = response.css('[rel="next"]::attr(href)').get()
        if(next_page is not None):
            next_page_url = "https://www.chocolate.co.uk"+next_page
            yield response.follow(next_page_url,callback=self.parse)