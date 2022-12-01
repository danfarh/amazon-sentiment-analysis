
import scrapy

review_url = 'https://www.amazon.com/product-reviews/{}'

product_list_woman_1 = ['B0169P8Y1Q', 'B078RK1RJ2', 'B0823H7DXH', 'B079ZZC81K', 'B081GCF2QC']
product_list_woman_2 = ['B071K9P1MZ', 'B0711CSPNG', 'B07L4DT2HZ', 'B074SZX5K8', 'B016YKKHOI', 'B00SCD250K', 'B07QM6YH1G', 'B07DX77ZV7', 'B016YKL66G', 'B077R7LV2K']

class AmazonReviewSpider(scrapy.Spider):
    name = 'amazon_review'
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    def start_requests(self):
        for product in product_list_woman_2:
            url = review_url.format(product)
            yield scrapy.Request(url)

    def parse(self, response):
        for review in response.css('[data-hook="review"]'):
            item = {
                'stars': review.css('[data-hook="review-star-rating"] span ::text').get(),
                'title': review.css('[data-hook="review-title"] span ::text').get(),
                'body': review.xpath('normalize-space(.//*[@data-hook="review-body"])').get()
            }
            
            yield item
        
        next_page = response.xpath('//a[text()="Next page"]/@href').get()
        
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))
