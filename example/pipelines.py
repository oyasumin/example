# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from scrapy import Item
import pymysql


class PriceConverterPipeline():
    # 英镑对人民币汇率
    exchange_rate = 8.5309

    def process_item(self, item, spider):
        # 提取item的price字段（如英镑53.74）
        # 去掉前边的英镑符号，转换为float类型，乘以汇率
        price = float(item['price'][1:])*self.exchange_rate

        # 保留两位小数
        item['price'] = "%.2f" % price

        return item

class DuplicatePipeline():
    def __init__(self):
        self.book_set = set()

    def process_item(self, item, spider):
        name = item['name']
        if name in self.book_set:
            raise DropItem("Duplicate book found:%s" % item)

        self.book_set.add(name)
        return item

class MysqlDBPipeline():
    # MYSQL_DB_NAME = 'scrapy_data'
    # MYSQL_HOST = '127.0.0.1'
    # MYSQL_PORT = 3306
    # MYSQL_USER = 'root'
    # MYSQL_PASSWORD = 'canon'

    @classmethod
    def from_crawler(cls, crawler):
        # 读取配置文件中的变量（不存在使用get方法里的默认值）
        cls.MYSQL_DB_NAME = crawler.settings.get("MYSQL_DB_NAME", "scrapy_data")
        cls.MYSQL_HOST = crawler.settings.get("MYSQL_HOST", "127.0.0.1")
        cls.MYSQL_PORT = crawler.settings.get("MYSQL_PORT", 3306)
        cls.MYSQL_USER = crawler.settings.get("MYSQL_USER", "root")
        cls.MYSQL_PASSWORD = crawler.settings.get("MYSQL_PASSWORD", "canon")
        return cls()

    def open_spider(self, spider):
        self.db_conn = pymysql.connect(host=self.MYSQL_HOST, port=self.MYSQL_PORT, db=self.MYSQL_DB_NAME, user=self.MYSQL_USER, passwd=self.MYSQL_PASSWORD, charset='utf8')
        self.db_cur = self.db_conn.cursor()

    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    def process_item(self, item, spider):
        values = (item['name'], item['price'])
        sql = 'INSERT INTO books VALUES (%s,%s)'
        self.db_cur.execute(sql, values)
        return item

class ExamplePipeline:
    def process_item(self, item, spider):
        return item


