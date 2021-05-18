import scrapy
from scrapy import Request
import pandas as pd
import os

df = pd.read_csv('asin_modified.csv')

# reviews_url = 'https://www.amazon.in/product-reviews/{}?filterByStar=positive'
reviews_url = 'https://www.amazon.in/product-reviews/{}?filterByStar=critical'

#asin_list = ['B08L8BJ9VC', 'B08445PP98']

asin_list = list(df['asin'].values)

class AmazonSpider(scrapy.Spider):
    name = 'amazon'

    def start_requests(self):
        try:
            for asin in asin_list:
                yield Request(reviews_url.format(asin))
        except:
            pass        

    def parse(self, response):
        try:
            reviews = response.css('[data-hook="review"]')
            for review in reviews:
                item = {
                    'Reviewer name': review.css('.a-profile-name::text').get(),
                    'title': review.css('[data-hook="review-title"] span::text').get(),
                    'Review body': review.xpath('normalize-space(.//*[@data-hook="review-body"])').get(),
                    'Review rating': review.css('[data-hook="review-star-rating"] span::text').get(),
                }

                yield item

            next_page = response.xpath('//a[text()="Next page"]/@href').get()
            if next_page:
                yield Request(response.urljoin(next_page))

        except:
            pass