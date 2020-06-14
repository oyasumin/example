# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

class BookItem(Item):
    name = Field()
    price = Field()

class ForeignBookItem(BookItem):
    translator = Field()

book = ForeignBookItem()
book['name'] = "巴黎圣母院"
book['price'] = 20.0
book['translator'] = "某人"

print(book)

class ExampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
