# -*- coding:utf-8 -*-
import redis
import base64
import json
import math
import time
import re
import datetime
import urllib
import random
import urljoin
import uuid
from lxml import etree
import MySQLdb
import os
import logging
import jieba
import jieba.analyse

logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
# A handler class which writes formatted logging records to disk files.
handler = logging.FileHandler("log_split.txt")
# 文件记录的日志级别
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)s ')
handler.setFormatter(formatter)
logger.addHandler(handler)

cur_path = os.path.dirname(__file__)

class KeyWords:
    def __init__(self):
        self.db = MySQLdb.connect(host="127.0.0.1",user="root",passwd="root",db='qust', charset='utf8')
        # 设置返回类型是字典
        self.cursor = self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)

        self.table = "detail_info"
        self.list_table = "list_info"

        self.limit = 1

    def get_content_from_database(self):
        select_sql = '''select * from {} where isparsed="0" limit {}'''.format(self.table, self.limit)
        self.cursor.execute(select_sql)
        data = self.cursor.fetchall()
        dict_data = [item for item in data if item is not None]
        for item in dict_data:

            # dict_post = json.loads(str_urls)
            id = item.get("id")
            uuid = item.get("uuid")
            content = item.get("content")
            # keywords = self.get_keyword(content)
            post = {
				"uuid":uuid,
				"content":content
			}

            self.update_keyword(post)
        return None


    def get_keyword(self,content):
        return jieba.analyse.extract_tags(content, topK=5, withWeight=False, allowPOS=('an')).__str__()

    def update_keyword(self,post):
        update_sql = '''update {} set isparsed="{}", keywords = "{}" where uuid = "{}"'''.format(self.table, 1,
                                                                                              self.get_keyword(
                                                                                                  post.get("content")),
                                                                               post.get("uuid"))
        print(update_sql)
        try:
            self.cursor.execute(update_sql)
            self.db.commit()
            print("修改keyword成功")
            logging.info("修改keyword成功")
        except Exception as e:
            print(e)
            self.db.rollback()


if __name__ == '__main__':
    keywords = KeyWords()
    while(1):
        keywords.get_content_from_database()
        continue
