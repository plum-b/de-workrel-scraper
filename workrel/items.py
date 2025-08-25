import scrapy

class WorkRelItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    snippet = scrapy.Field()
    date = scrapy.Field()
    source_page = scrapy.Field()
