# -*- coding:utf-8 -*-
import copy
import requests
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
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
import logging

# 日志对象（设置日志名，等级）->handler对象（设置日志文件名，记录等级）->设置format->formatter对象和handler绑定->handler对象和logger对象绑定

logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
# A handler class which writes formatted logging records to disk files.
handler = logging.FileHandler("log_ouc_list.txt")
# 文件记录的日志级别
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)s ')
handler.setFormatter(formatter)
logger.addHandler(handler)

cur_path = os.path.dirname(__file__)



class MySpider():
    def __init__(self):

        # 网站名称
        self.siteName = "中国海洋大学就业指导中心"
        # 类别码，01新闻、02论坛、03博客、04微博 05平媒 06微信  07 视频、99搜索引擎
        self.info_flag = "99"

        # 入口地址列表
        # self.start_urls = ["http://www.bidcenter.com.cn/viplist-1.html"]
        self.start_urls = ["http://career.ouc.edu.cn"]
        self.encoding = 'utf8'
        self.site_domain = 'ouc.edu.cn'
        self.dedup_uri = None
        self.headers = {

        "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",


        }

        self.request_headers = {'headers': self.headers}
        try:
            # self.conn = redis.StrictRedis.from_url ('redis://192.168.1.34/5')
            self.conn = redis.StrictRedis.from_url ('redis://127.0.0.1/5')
        except:
            self.conn = None
        # self.db = DB ().create ('mysql://zhxg:ZHxg2017!@192.168.1.19:3306/sjk')
        self.db = MySQLdb.connect(host="188.131.252.159",user="root",passwd="root",db='qust', charset='utf8')
        # self.db = MySQLdb.connect(host="localhost",user="root",passwd="root",db='qust', charset='utf8')
        self.cursor = self.db.cursor ()

        # self.db = DB ().create ('mysql://root:1234@localhost:3306/sjk')
        self.limits = 1
        self.deal_stage = ""
        self.timekey = ""
        # self.get_key_urls="list:page_search_ggzy_url"
        self.sess = requests.session()
        # self.proxy = self.proxy_random()
        self.table = "list_info"

    def parse(self, url=None):

        # print str(self.proxy)
        if url:
            # self.keywords = re.findall ("keywords=(.*?)&", url)[0]
            res = self.get_download(url)
            self.parse_detail_page(res)
        return

    def get_download(self,url):
        try:
            res = self.sess.post (url, headers=self.headers, verify=False, timeout=20)
            print("get_download")
            # res = self.sess.get(url,headers =self.headers,verify =False,timeout=20)
        except Exception as e:
            print(e)
            try:
                logger.info ("请求第二次%s " % url)
                print("下载第二次",url)
                res = self.sess.get (url, headers=self.headers, verify=False,
                                     timeout=20)
            except:
                time.sleep (3)
                try:
                    logger.info ("请求第三次%s " % url)
                    res = self.sess.get (url, headers=self.headers, verify=False,
                                         timeout=20)
                except:
                    time.sleep (3)

                    res = ''
        return res



    def parse_detail_page(self, response=None, url=None):
        try:
            response.encoding = self.encoding
            unicode_html_body = response.text
            # print(unicode_html_body)
            dict_content = json.loads(unicode_html_body)

            data = dict_content["items"]

            # data = etree.HTML(unicode_html_body)
            # data =BeautifulSoup(unicode_html_body,"lxml")
            # data = htmlparser.Parser (unicode_html_body)

        except Exception as e:
            print("parse_detail_page(): %s" % e)
            return None
        from_tag_url = response.url
        logger.info("list page url%s" % from_tag_url)
        #
        # li_content = data.xpath('''//li[@class="l-twos"]''')
        for item in data:
            detail_url = "http://career.ouc.edu.cn/zftal-web/zfjy!wzxx!zghydx10423/xjhxx_ckXjhxx.html?sqbh="+item["sqbh"]
            if self.getdumps(detail_url):
                continue
            date = item["sqsj"]
            location = item["xjhcdmc"]
            uid = str(uuid.uuid3(uuid.NAMESPACE_DNS, detail_url.decode('utf-8', errors='ignore').encode('utf-8'))) + str(uuid.uuid5(uuid.NAMESPACE_DNS, detail_url.decode('utf-8', errors='ignore').encode('utf-8')))[0]
            ctime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            title = item["xjhmc"]
            siteName = self.siteName
            post = {
                "uuid": uid,  # md5
                "detailUrl": detail_url,  # url
                "title": title,  # 标题
                "location": location,  # 地点
                "siteName": self.siteName,
                "ctime": ctime,
                "date": date,

            }

            dic = self.handle_post(post)
            sql = '''insert into list_info (uuid,detailUrl,title,location,siteName,ctime,date)
                                      VALUE (%s,%s,%s,%s,%s,%s,%s);'''
            try:
                # 执行sql语句
                self.db.ping()

            except Exception as e:
                logger.info(e)
                self.db.rollback()  # 捕捉到错误就回滚
                self.db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="root", db='qust',
                                          charset='utf8')

            try:
                self.cursor.execute(sql, (
                    uid, detail_url, title, location, siteName, ctime, date))
                self.db.commit()  # 把修改的数据提交到数据库
                logger.info("入库完成")
            except Exception as e:
                logger.info(e)
                self.db.rollback()  # 捕捉到错误就回滚

        # self.parse_restore(unicode_html_body)
        return

    def __del__(self):
        try:
            self.cursor.close()
            self.db.close()
        except Exception as  e:
            logger.info(e)
            print(e)

    def getdumps(self, url):
        if self.conn.sismember("dumps:ouc", url):
            return True  # 在里面
        else:
            print
            "入redis：去重库"
            self.conn.sadd("dumps:ouc", url)
            return False

    def handle_post(self, post):
        post = copy.deepcopy(post)
        for k, v in post.items():
            print(k,v)
            if not isinstance(v, str) and not isinstance(v, int) and not isinstance(v, float):
                v = json.dumps(v)
            try:
                v = MySQLdb.escape_string(v)
            except:
                pass
            post.update({k: v})
        return post

def mm():
    spider = MySpider()

    # try:
    spider.parse("http://career.ouc.edu.cn/zftal-web/zfjy!ykfw!zghydx10423/xjhxx_cxXjhListQtcx.html?doType=query")
    # except Exception as e:
    #     logger.info(e)
    #     print(e)


if __name__ == '__main__':
    mm()
    # spider = MySpider ()
    # url ="https://www.chinabidding.cn/search/Searchgj/zbcg?table_type=&text_x=%E8%BE%93%E5%85%A5%E6%82%A8%E6%83%B3%E6%9F%A5%E6%89%BE%E7%9A%84%E5%85%B3%E9%94%AE%E8%AF%8D+%E5%A4%9A%E4%B8%AA%E8%AF%8D%E5%8F%AF%E4%BB%A5%E8%BE%93%E5%85%A5%E7%A9%BA%E6%A0%BC%E9%9A%94%E5%BC%80%EF%BC%81&keywords=%E4%BA%A4%E9%80%9A%20%E8%A7%84%E5%88%92&search_type=TITLE&areaid=&categoryid=&b_date=custom&time_start=2019-01-14&time_end=2019-01-14"
    # # # urll ="https://www.chinabidding.cn/search/searchgj/zbcg?areaid=&keywords=总承包&time_start=2019-01-14&time_end=2019-01-14&page=2&search_type=TITLE&categoryid=&rp=30&table_type=&b_date=custom"
    # spider.parse(url)

