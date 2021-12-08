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
    def parse_only_quotes(self, response, **kwargs):
        if kwargs:
            quotes = kwargs['quotes']
            authors = kwargs['authors']
        quotes.extend(response.xpath('//span[@class = "text" and @itemprop = "text"]/text()').getall())
        authors.extend(response.xpath('//small[@class="author"]/text()').getall())
          #Button to next page
        next_page_button_link = response.xpath('//li[@class = "next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs = {'quotes':quotes, 'authors':authors})
        else:
            quotes_author = []
            i=0
            for i in range(len(quotes)):
                quotes_author.append({'Quote':quotes[i], 'Author':authors[i]})
            yield{'quotes':quotes_author}



    

    def parse(self, response):
        title = response.xpath('//h1/a/text()').get()
        quotes = response.xpath('//span[@class = "text" and @itemprop = "text"]/text()').getall()
        authors = response.xpath('//small[@class="author"]/text()').getall()
        top_tags = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()
        #Save top tags
        top = getattr(self, 'top', None)
        if top:
            top = int(top)
            top_tags = top_tags[:top]


        yield {'Title': title,
                'Top tags': top_tags}
        #Button to next page
        next_page_button_link = response.xpath('//li[@class = "next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs = {'quotes':quotes, 'authors':authors})
        else:
            quotes_author = list(zip(quotes, authors))
            yield{
                'quotes': quotes_author}

