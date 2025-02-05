# -*- coding:utf-8 -*-
import datetime
from GXNUDiagSystem import GXNUDiagSystem
# import schedule
import time
import os
import subprocess
import psutil

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

# kill clash
def kill_process_by_name(process_name):
    """
    通过程序名称退出正在运行的 .exe 程序
    :param process_name: 目标程序名称 (如 "notepad.exe")
    """
    try:
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == process_name:
                print(f"找到进程: {proc.info}, 正在终止...")
                proc.terminate()  # 终止进程
                proc.wait()  # 等待进程结束
                print(f"已成功终止进程: {process_name}")
                return
        print(f"未找到目标程序: {process_name}")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == '__main__':
    conn()
    # schedule.every(30).minutes.do(conn)

    while True:

        # 先退出 clash
        target_program = "Clash Verge.exe"  # 替换为你的 .exe 程序名
        kill_process_by_name(target_program)
        
        # 每隔半小时连接一次
        time.sleep(1800)
        conn()
        # schedule.run_pending()
