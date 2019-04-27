# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import MySQLdb
import os
import logging
import jieba
import jieba.analyse
import chardet
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
        self.db = MySQLdb.connect(host="188.131.252.159",user="root",passwd="root",db='qust', charset='utf8')
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
        result =  jieba.analyse.extract_tags(content, topK=5, withWeight=False, allowPOS=('an'),)
        list = [item.encode('utf-8') for item in result]

        return "/".join(result)
    def update_keyword(self,post):
        update_sql = '''update {} set isparsed="{}", keywords = "{}" where uuid = "{}"'''.format(self.table, 1,
                                                                                              self.get_keyword(
                                                                                                  post.get("content")),
                                                                               post.get("uuid"))

        update_sql2 = '''update {} set keywords = "{}" where uuid = "{}"'''.format(self.list_table,
                                                                                                 self.get_keyword(
                                                                                                     post.get(
                                                                                                         "content")),
                                                                                                 post.get("uuid"))
        try:
            self.cursor.execute(update_sql)
            self.cursor.execute(update_sql2)
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