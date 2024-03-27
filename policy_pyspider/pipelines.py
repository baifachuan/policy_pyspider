# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from policy_pyspider.items import PolicyPyspiderItem
import pymysql

from policy_pyspider.settings import MYSQL_HOST, MYSQL_DBNAME, MYSQL_PASSWORD, MYSQL_USER, MYSQL_PORT


class PolicyPyspiderPipeline:
    def process_item(self, item, spider):
        if isinstance(item, PolicyPyspiderItem):
            self.save(item)
            return item
        else:
            raise DropItem("Not a PolicyPyspiderItem")

    def save(self, item):
        conn = pymysql.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DBNAME,
        )
        cursor = conn.cursor()
        cursor.execute("insert into policy(name, link, publishDate, policyType, reqeustURL) "
                       "values('{}', '{}', '{}', '{}', '{}')"
                       .format(item['name'], item['link'], item['publishDate'], item['policyType'], item['reqeustURL']))
        conn.commit()
        cursor.close()
