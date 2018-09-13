# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, Join, TakeFirst
from w3lib.html import remove_tags, remove_tags_with_content


def remove(text, loader_context):
    return remove_tags(remove_tags_with_content(
        text, which_ones=('span', 'sup', 'div')))


class Chapter(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=TakeFirst()
    )
    para = scrapy.Field(
        input_processor=MapCompose(remove),
        output_processor=Join()
    )
