from xxh_qust_list import MySpider
import logging
import datetime
import time
import random
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("log_qust_list.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
if __name__ == '__main__':

    spider = MySpider()
    while 1:
        spider.parse("http://job.qust.edu.cn/index.php?route=shuangxuanhui/xuanjianghui_list")
        # a = datetime.datetime.now().hour
        # if 0 <= a <= 6:
        #     time.sleep(600)
        #     continue
        # else:
        sleepTime = random.choice(range(12*60*60, 13*60*60))
        print("sleep "+str(sleepTime)+" seconds")
        time.sleep(sleepTime)

        continue
            # a = datetime.datetime.now().hour
            # # print a
            # if 0 <= a <= 7:
            #     time.sleep(600)
            #     continue
            # else:

