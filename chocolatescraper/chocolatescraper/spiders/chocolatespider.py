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
            chocolate.add_css('name','div.product-item-meta a::text'),
            chocolate.add_css('price',product.css('span.price').get().replace('<span class="price">\n              <span class="visually-hidden">Sale price</span>',"").replace('</span>',""),
            Chocolate['url']=product.css('div.product-item-meta a').attrib['href']
            yield chocolate
            
        
        next_page = response.css('[rel="next"]::attr(href)').get()
        if(next_page is not None):
            next_page_url = "https://www.chocolate.co.uk"+next_page
            yield response.follow(next_page_url,callback=self.parse)