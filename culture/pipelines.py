# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import redis
import culture.config.redisconf as rc


class CulturePipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.collection_name = 'test'

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri='mongodb://localhost:27017/',
            mongo_db='poetry'
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item


class RedisPipeline(object):
    def __init__(self, host, port, password):
        self.host = host
        self.port = port
        self.password = password

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=rc.conf['host'],
            port=rc.conf['port'],
            password=rc.conf['password']
        )

    def open_spider(self, spider):
        self.client = redis.StrictRedis(
            host=self.host, port=self.port, db=0, password=self.password, decode_responses=True)

    def close_spider(self, spider):
        print('close')

    def process_item(self, item, spider):
        self.client.set(item['name'], item['para'])
