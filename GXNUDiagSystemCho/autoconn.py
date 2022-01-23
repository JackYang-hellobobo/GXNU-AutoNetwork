# -*- coding:utf-8 -*-
import datetime
from GXNUDiagSystem import GXNUDiagSystem
import schedule
import time
import os


class Logger(object):
    def __init__(self, output_name):
        dirname = os.path.dirname(output_name)
        if not os.path.exists(dirname):
            os.mkdir(dirname)

        self.log_file = open(output_name, 'a+')

    def write(self, msg):
        self.log_file.write(msg + '\n')
        self.log_file.flush()
        print(msg)


diag = GXNUDiagSystem()
logger = Logger(os.path.join('.', 'log.txt'))


def conn():
    checkConn = diag.checkAlive()
    if not checkConn:
        logger.write("检测没有连接成功！")
        login_res = diag.login()
        while not login_res:
            localtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            logger.write("%s 登录失败\n" % localtime)
            login_res = diag.login()
            time.sleep(10)

        localtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.write("="*30 + '\n')
        logger.write("%s 登录成功\n" % localtime)
        logger.write("="*30 + '\n')
    else:
        localtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.write("%s 保持在线\n" % localtime)


if __name__ == '__main__':
    conn()
    # schedule.every(30).minutes.do(conn)

    while True:
        time.sleep(1800)
        conn()
        # schedule.run_pending()
