# -*- coding:utf-8 -*-
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")
from xxh_qust_detail import MySpider
import logging
import datetime
import time
import random
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("log_qust_detail.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
if __name__ == '__main__':

    spider = MySpider()
    while 1:
        spider.parse()
        a = datetime.datetime.now().hour
        if 0 <= a <= 6:
            time.sleep(600)
            continue
        else:
            time.sleep(random.choice(range(80, 100)))

            # a = datetime.datetime.now().hour
            # # print a
            # if 0 <= a <= 7:
            #     time.sleep(600)
            #     continue
            # else:

