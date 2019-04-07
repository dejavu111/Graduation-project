
# 采集的列表页，得到的结果为链接，标题，时间，地区
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
from bs4 import BeautifulSoup
import MySQLdb
import sys


import os
import logging
# import pymysql

from lxml import etree

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("log_qust_detail.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

cur_path = os.path.dirname(__file__)



def getText(elem):
    rc = []
    for node in elem.itertext():
        rc.append(node.strip())
    return ''.join(rc)



class MySpider():

    def __init__(self):

        # 网站名称
        self.siteName = "青岛科技大学就业指导中心"
        # 类别码，01新闻、02论坛、03博客、04微博 05平媒 06微信  07 视频、99搜索引擎
        self.info_flag = "99"

        # 入口地址列表
        # self.start_urls = ["http://www.bidcenter.com.cn/viplist-1.html"]
        self.start_urls = ["http://job.qust.edu.cn"]
        self.encoding = 'utf8'
        self.site_domain = 'qust.edu.cn'
        self.dedup_uri = None

        # self.request_headers = {'headers': self.headers}
        try:
            # self.conn = redis.StrictRedis.from_url('redis://192.168.1.34/3')
            self.conn = redis.StrictRedis.from_url('redis://localhost/5')
        except:
            self.conn = None
        # self.db = DB ().create ('mysql://zhxg:ZHxg2017!@192.168.1.19:3306/sjk')
        self.db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="root", db='qust', charset='utf8')
        self.cursor = self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        # a = self.conn.get("cookie:chinabidding")
        # aa = json.loads(a)
        # b = []
        # for k, v in aa.iteritems():
        #     b.append('{}={}'.format(k, v))
        # c = ";".join(b)
        # print c
        self.headers = {

            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",

        }

        self.table = "list_info"
        self.base2 = "detail_info"

        self.sess = requests.session()
        self.encoding = "utf-8"


    def parse(self, url=None):
        '''
        抓取列表页下所有详情页的链接
        '''

        sql = '''select * from list_info where isparsed = "0" and siteName = "青岛科技大学就业指导中心" limit 3'''
        self.cursor.execute(sql)
        urls = self.cursor.fetchall()
        dict_page_info = [url for url in urls if url is not None]
        # print "********-->",len(dict_page_info)
        for str_urls in dict_page_info:

            # dict_post = json.loads(str_urls)
            dict_post = str_urls
            id = dict_post.get("id")
            detailUrl = dict_post.get("detailUrl")
            logger.info(detailUrl)
            siteName = dict_post.get("siteName")
            uuid = dict_post.get("uuid")
            statue, data = self.get_detailpage(detailUrl)
            if 0 == statue:
                return
            if data is not None:

                contents = data.xpath(
                    '''//ul[@class="x-xul"][1]//text()''') # 内容
                content = ''
                for i in contents:
                    content += i.strip() + ' '

                content = self.makecontent(content)
                ctime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                holdTime = data.xpath('''//div[@class="x-zwkn"]//tr[@class="x-tatrs"][1]//p[@class="x-tatdb"]/text()''')[0]
                companyInfos = data.xpath('''//ul[@id="ul_customers"]//text()''')
                companyInfo = ''
                for i in companyInfos:
                    companyInfo += i.strip() + ' '
                jobList = data.xpath('''//ul[@id="ul_zhiweis"]//li''')
                num = len(jobList)
                print(num)
                print(detailUrl)
                post = {
                    "uuid": uuid,  # md5
                    "detailUrl": detailUrl,  # url
                    "title": dict_post.get("title"),  # 标题
                    "location": dict_post.get("location"),  # 举办地点
                    "holdTime": holdTime,  # 举办时间
                    "siteName": self.siteName,  # 域名名稱
                    "ctime": ctime,  # 采集時間
                    "content": content,
                    "companyInfo":companyInfo,

                }

                # for k,v in post.iteritems():
                #     print k,v
                dic = self.handle_post(post)
                sql = '''insert into detail_info (uuid,detailUrl,title,location,holdTime,siteName,ctime,content,companyInfo)
                           VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
                try:
                    # 执行sql语句
                    self.cursor.execute(sql, (
                         uuid, detailUrl, dict_post.get("title"), dict_post.get("location"),
                        holdTime,
                         self.siteName, ctime, content,
                         companyInfo))
                    for i in range(1,num+1):
                        jobName = \
                        data.xpath('''//ul[@id="ul_zhiweis"]//li[{}]//p[@class="x-szhi-1"]/a/text()'''.format(i))
                        if jobName:
                            jobName = jobName[0]
                        else:
                            jobName = data.xpath('''//ul[@id="ul_zhiweis"]//li[{}]//p[@class="x-szhi-1"]/text()'''.format(i))
                            if jobName:
                                jobName = jobName[0]
                            else:
                                jobName = ""
                        jobLocation = \
                        data.xpath('''//ul[@id="ul_zhiweis"]//li[{}]//p[@class="x-szhi-1"]/text()'''.format(i))
                        if jobLocation:
                            jobLocation = jobLocation[0]
                        else:
                            jobLocation = ""
                        if "[" not in jobLocation:
                            jobLocation = ""
                        jobRequirements = \
                        data.xpath('''//ul[@id="ul_zhiweis"]//li[{}]//p[@class="x-szhi-2"]/text()'''.format(i))
                        if jobRequirements:
                            jobRequirements = jobRequirements[0].replace("&nbsp ","")
                        else:
                            jobRequirements = ""
                        jobSalary = \
                        data.xpath('''//ul[@id="ul_zhiweis"]//li[{}]//p[@class="x-szhi-2"]/span/text()'''.format(i))
                        if jobSalary:
                            jobSalary = jobSalary[0]
                        else:
                            jobSalary = ""
                        if "k" not in jobSalary:
                            jobSalary = ""
                        jobCompany = \
                        data.xpath('''//ul[@id="ul_zhiweis"]//li[{}]//p[@class="x-szhi-3"]//text()'''.format(i))
                        if jobCompany:
                            jobCompany = jobCompany[0]
                        else:
                            jobCompany = ""
                        sql = '''insert into job (uuid,jobName,jobLocation,jobRequirements,jobSalary,jobCompany)
                        VALUE (%s,%s,%s,%s,%s,%s);'''
                        self.cursor.execute(sql,(uuid,jobName,jobLocation,jobRequirements,jobSalary,jobCompany))

                    self.cursor.execute('update list_info set isparsed="1" where uuid = "{0}"'.format(uuid))
                    self.db.commit()  # 把修改的数据提交到数据库
                    print("入库成功")
                    logger.info("入库完成")
                except Exception as e:
                    print(e)
                    self.db.rollback()  # 捕捉到错误就回滚
                    update_sql = 'update list_info set isparsed = "0" where uuid = "{0}" '.format(uuid)
                    self.cursor.execute(update_sql)
                    self.db.commit()



            else:

                self.db.commit()

        uu = []
        return (uu, None, None)

    def get_detailpage(self, detailUrl):

        response = requests.get(url=detailUrl, headers=self.headers, verify=False)
        try:
            response.encoding = "utf-8"

            unicode_html_body = response.text
            data = etree.HTML(unicode_html_body)
            # data = htmlparser.Parser (unicode_html_body)
        except Exception as e:
            return []

        if data is not None:
            return True, data

    def handle_post(self, post):
        post = copy.deepcopy(post)
        for k, v in post.items():
            if not isinstance(v, str) and not isinstance(v, int) and not isinstance(v, float):
                v = json.dumps(v)
            try:
                v = MySQLdb.escape_string(v)
            except:
                pass
            post.update({k: v})
        return post

    def makecontent(self, content):
        # print "before:", content
        content = re.sub(" |\t|\n|\r|\r\n", "", content).strip()
        content = content.replace(" ", "").strip()
        content = ''.join(content.split(" "))
        # print "after", content
        return content



if __name__ == '__main__':
    spider = MySpider()

    spider.parse()
    # spider.proxy_enable = False
    # spider.init_dedup()
    # spider.init_downloader()
    # ------------ parse() ----------
    # print "开始登录"
    # url = "https://www.chinabidding.com.cn/"
    # resp = spider.download(url)
    # res = spider.parse(resp, url)

    # ------------ parse_detail_page() ----------
    # url = "http://www.bidcenter.com.cn/zbpage-4-%E6%B1%9F%E8%8B%8F-1.html"
    # resp = spider.download(url)
    # res = spider.parse_detail_page(resp, url)
    # for item in res:
    #     for k, v in item.iteritems():
    #         print k, v




