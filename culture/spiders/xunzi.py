# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from culture.items import Chapter


class XunziSpider(scrapy.Spider):
    name = 'xunzi'
    domain = 'https://ctext.org/'
    start_urls = ['https://ctext.org/xunzi/zhs']

    def parse(self, response):
        links = response.xpath(
            '//div[@id="content2"]/a[contains(@href,"xunzi/")]/@href').extract()
        for link in links:
            yield scrapy.Request(url=self.domain + link, callback=self.parsechapter)

    def parsechapter(self, response):
        chapter = ItemLoader(item=Chapter(), response=response)
        chapter.add_xpath(
            'name', '//div[@id="content3"]/table[1]/tr/td/h2/text()')
        chapter.add_xpath('para', '//div[@id="content3"]/table[2]/tr/td[3]')
        return chapter.load_item()
