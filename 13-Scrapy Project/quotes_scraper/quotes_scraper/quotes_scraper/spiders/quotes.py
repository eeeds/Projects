import scrapy

#Titulo = //h1/a/text()
#Citas = //span[@class = "text" and @itemprop = "text"]/text()
#Top ten tags= //div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()
#next page button = //li[@class = "next"]/a/@href

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]
    #Export to json file
    custom_settings = {
        'FEEDS': {
            'quotes.json': {
                'format': 'json',
                'encoding': 'utf8',
                'store_empty': False,
                'fields': None,
                'indent': 4,
                'item_export_kwargs': {
                    'export_empty_fields': True,
                },
            },
        },
    }

    def parse(self, response):
        title = response.xpath('//h1/a/text()').get()
        quotes = response.xpath('//span[@class = "text" and @itemprop = "text"]/text()').getall()
        top_ten_tags = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()


        yield {'Title': title, 
                'Citas': quotes, 
                'Top ten tags': top_ten_tags}
        #Button to next page
        next_page_button_link = response.xpath('//li[@class = "next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse)

