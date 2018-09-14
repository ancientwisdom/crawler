from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

process = CrawlerProcess(get_project_settings())
process.crawl('xunzi')
process.start()
